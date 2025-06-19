from mr.prompt import MeterBoxPrompt, TextBoxPrompt


def test_prompt():
  prompt = MeterBoxPrompt()
  assert prompt.get_prompt() is not None

  prompt = TextBoxPrompt()
  assert prompt.get_prompt() is not None
