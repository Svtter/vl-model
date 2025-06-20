from mr.vlask import VlAsk


def test_read():
  vlask = VlAsk("openai/gpt-4o")
  result = vlask.ask("resources/image.jpg")
  print(result)
