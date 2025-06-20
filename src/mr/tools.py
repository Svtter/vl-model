from mr.group import ModelGroup, siliconflow_group
from vl_model.client import get_client


class JSONFormatter(object):
  def __init__(self, group: ModelGroup = siliconflow_group):
    self.client = get_client()
    self.group = group

  def format_response(self, content: str) -> str:
    response = self.client.chat.completions.create(
      model=self.group.fast,
      messages=[
        {
          "role": "system",
          "content": (
            "You are a helpful assistant. "
            "You can make the json content more readable and concise. "
            "Only return the json content, no other text. "
            "no ```json```. "
          ),
        },
        {
          "role": "user",
          "content": f"Please format the following json content: {content}",
        },
      ],
    )
    return response.choices[0].message.content or ""
