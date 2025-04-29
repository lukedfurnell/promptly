import os
from promptly.main import prompts_md

def test_prompts_md(tmp_path):
    os.chdir(tmp_path)
    prompts_md(" This is a test prompt ")
    content = (tmp_path / "prompts.md").read_text()
    
    assert "This is a test prompt" in content