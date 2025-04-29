from promptly.main import meta_prompt

class FakeClient:
    class responses:
        @staticmethod
        def create(model, instructions, input):
            return type("Response", (), {"output_text": "mocked output"})()

def test_meta_prompt():
    assert meta_prompt(FakeClient(), "some prompt", "some input") == "mocked output"