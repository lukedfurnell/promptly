#!/usr/bin/env python3
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os, sys
from pathlib import Path
from .meta_prompt    import metaprompt
from .grading_prompt import grading_prompt
from datetime import datetime
from .grading_test import grade_prompt

def load_api_key():

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            sys.stderr.write(
                "Error: OPENAI_API_KEY not set.\n"
                "Please run: export OPENAI_API_KEY=\"your_api_key\"\n"
            )
            sys.exit(1)

        return api_key

def get_user_inputs():

        user_prompt      = input("  Prompt:\n> ").strip().lower()
        file_name_prompt = input("  Context:\n> ").strip()
        
        valid_verbosity_levels = ["low", "medium", "high"]
        verboseness = ""
        while verboseness not in valid_verbosity_levels:
            verboseness = input("  Verboseness (low/medium/high):\n> ").strip().lower()
            if verboseness not in valid_verbosity_levels:
                print("  Please enter a valid verbosity level: low, medium, or high")

        return user_prompt, file_name_prompt, verboseness

def find_file(file_name_prompt):

    cwd = Path.cwd().resolve()

    # Try direct file path first (atomic operation)
    try:
        potential_path = cwd / file_name_prompt
        file_path = potential_path.resolve(strict=False)

        # Ensure the resolved path is within the working directory
        if not str(file_path).startswith(str(cwd)):
            sys.stderr.write("Error: Access denied to file outside working directory\n")
            sys.exit(1)

        # Check if it's a file within a single atomic block
        if file_path.is_file():
            return file_path
        
    except (ValueError, OSError) as e:
        sys.stderr.write(f"Error processing file path: {e}\n")
        sys.exit(1)

    # Try glob pattern with timeout protection
    try:
        # Convert dangerous glob patterns to safer versions
        safe_pattern = file_name_prompt.replace('*', '[*]').replace('?', '[?]')
        if safe_pattern != file_name_prompt:
            # If pattern was modified, it contained potentially unsafe wildcards
            file_path = next(cwd.glob(safe_pattern), None)
        else:
            # Original pattern was safe, proceed with glob but limit search depth
            max_depth = 5
            file_path = None

            for depth in range(1, max_depth + 1):
                pattern = "*/" * (depth - 1) + file_name_prompt
                file_path = next(cwd.glob(pattern), None)
                if file_path:
                    break

            if file_path:
                safe_path = file_path.resolve(strict=False)

                # Ensure the found path is within the working directory
                if not str(safe_path).startswith(str(cwd)):
                    sys.stderr.write("Error: Access denied to file outside working directory\n")
                    sys.exit(1)

                if safe_path.is_file():
                    return safe_path
                
    except (ValueError, OSError) as e:
        sys.stderr.write(f"Error with glob pattern: {e}\n")
        sys.exit(1)

    sys.stderr.write(f"Error: File not found: {file_name_prompt}\n")
    sys.exit(1)

def read_file(file_path):

    contents = file_path.read_text()

    return contents

def meta_prompt(client, filled_prompt, user_prompt):

        response = client.responses.create(
            model="gpt-4.1",
            instructions=filled_prompt,
            input=user_prompt
        )
    
        return response.output_text

def grab_meta_prompt(file_content, verboseness, user_prompt, extra ="", previous_prompt=""):

        filled_prompt = metaprompt.format(
            contents=file_content,
            verboseness=verboseness,
            extra=extra,
            previous_prompt = previous_prompt,
            user_prompt = user_prompt
        )

        return filled_prompt

def prompts_md(call_open_ai):
      
    with open("prompts.md", "a", encoding="utf-8") as f:
        f.write(
        f"## Prompt at {datetime.now():%Y-%m-%d %H:%M:%S}\n\n"
        f"{call_open_ai.strip()}\n\n"
    )
        
def main():

    client = OpenAI(api_key=load_api_key())

    previous_prompt = None

    while True:
        # Gather inputs
        user_prompt, file_name_prompt, verboseness = get_user_inputs()

        # Read context and build the meta‐prompt template
        file_path     = find_file(file_name_prompt)
        file_content  = read_file(file_path)
        meta_template = grab_meta_prompt(file_content, verboseness, user_prompt)

        #print("\n==== RAW META-PROMPT TEMPLATE ====\n", meta_template)

        # 1) Generate the first improved prompt

        improved = meta_prompt(client, meta_template, user_prompt)

        print("\n==== IMPROVED PROMPT ====\n", improved)

        # 2) Let them refine it as many times as they like

        previous_prompt = improved

        while True:
            ans = input("  Refine this prompt? (y/n):\n> ").strip().lower()
            if ans == "y":
                extra = input("  Enter refinement instructions:\n> ").strip()
                # Re-run the LLM call with those extra instructions appended
                meta_template = grab_meta_prompt(file_content, verboseness, user_prompt, extra, previous_prompt)

                #print("\n==== META PROMPT ====\n", meta_template)
                
                improved = meta_prompt(client, meta_template, user_prompt)

                print("\n==== REFINED PROMPT ====\n", improved)

                previous_prompt = improved
            else:
                break

        # 3) Now proceed with grading, saving, etc.
        grade, grading_payload = grade_prompt(
            user_prompt, grading_prompt, client, improved
        )
        print("\n==== GRADE TABLE ====\n", grade)

        prompts_md(improved)
        print("\nSaved this prompt to prompts.md\n")

        if input("Run another prompt? (y/n):\n> ").strip().lower() != "y":
            break

if __name__ == "__main__":
    main()




