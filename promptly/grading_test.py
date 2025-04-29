def grade_prompt(user_prompt, grading_prompt, client, call_open_ai):
        
        grading = (
            f"Human prompt: {user_prompt}\n\n"
            f"Meta prompt produced by chat gpt based on human's initial prompt: {call_open_ai}"
        )

        response = client.responses.create(
        model="gpt-4.1",
        input=grading,
        instructions=grading_prompt
        )

        return response.output_text, grading