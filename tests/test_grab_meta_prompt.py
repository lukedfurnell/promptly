from promptly.main import grab_meta_prompt
from promptly.meta_prompt  import metaprompt

def test_grab_meta_prompt():

    result = grab_meta_prompt("file content", "high", "more examples")

    expected = metaprompt.format(contents="file content", verboseness="high", extra="more examples")

    assert result == expected
