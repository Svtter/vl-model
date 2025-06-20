import json

from mr.group import siliconflow_group
from mr.tools import JSONFormatter


def test_json_formatter():
  dirty_json = """
  This is a dirty json:
  {'test': 'test'}
  """

  json_formatter = JSONFormatter(group=siliconflow_group)

  result = json_formatter.format_response(dirty_json)

  try:
    assert json.loads(result) == {"test": "test"}
  except json.JSONDecodeError:
    assert False, f"json.JSONDecodeError: {result}"
