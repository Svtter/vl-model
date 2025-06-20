from mr.tools import JSONFormatter


def test_json_formatter():
  dirty_json = """
  This is a dirty json:
  {'test': 'test'}
  """
  json_formatter = JSONFormatter()
  assert json_formatter.format_response(dirty_json) == """{"test": "test"}"""
