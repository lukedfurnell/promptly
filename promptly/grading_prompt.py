grading_prompt = """
You will compare two prompts—the original human prompt and the revised “meta” prompt—and score each from 1 to 10 on these key dimensions:

1. Role Usage: How well does the prompt employ developer/user message roles or instructions?  
2. Structure & Formatting: How clear and well-formatted are the sections (using Markdown headers or XML tags to delineate Identity, Instructions, etc.)?  
3. Examples: How effectively does it provide few-shot examples to steer the model?  
4. Context Inclusion: How well does it include or reference relevant external context or documents?

Return exactly one Markdown table in this format:

| Prompt       | Role Usage | Structure & Formatting | Examples | Context Inclusion |
|--------------|:----------:|:----------------------:|:--------:|:-----------------:|
| Human Prompt |     0-10   |         0-10           |   0-10   |       0-10        |
| Meta Prompt  |     0-10   |         0-10           |   0-10   |       0-10        |
"""

##maybe add goal here as a scoring criteria