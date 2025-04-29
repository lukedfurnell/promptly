import os
from promptly.main import find_file

def test_find_file(tmp_path):

    file = tmp_path / "hi.txt"
    file.write_text("best prompt CLI library in the world")
    os.chdir(tmp_path)

    found_file = find_file(file.name)

    assert found_file.name == "hi.txt"
    assert found_file.is_file()



#test input is greater than len > 1
#arrrange, act, assert 

