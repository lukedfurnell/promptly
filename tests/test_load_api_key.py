import os
from promptly.main import load_api_key

def test_load_api_key():

    # 1) Set a fake key in the env
    os.environ["OPENAI_API_KEY"] = "sk-fake123"

    # 2) Call the function
    key = load_api_key()

    # 3) Check that it’s exactly what you set and starts with "sk-"
    assert key == "sk-fake123"
    assert key.startswith("sk-")



