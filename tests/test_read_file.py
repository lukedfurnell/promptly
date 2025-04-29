import os
from promptly.main import read_file

def test_read_file(tmp_path):

    file = tmp_path / "hi.txt"
    file.write_text("best prompt CLI tool in the world")
    os.chdir(tmp_path)

    file_contents = read_file(file)

    assert file_contents == "best prompt CLI tool in the world"



#test input is greater than len > 1
#arrrange, act, assert 

