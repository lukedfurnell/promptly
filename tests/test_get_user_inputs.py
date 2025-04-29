import os
from promptly.main import get_user_inputs

def test_get_user_inputs():


    user_prompt, file_name_prompt, verboseness = get_user_inputs()

    assert user_prompt == "rewrite this file"
    assert file_name_prompt == "context.txt"
    assert verboseness == "low"



#test input is greater than len > 1
#arrrange, act, assert 

