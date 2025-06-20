from vl_model.client import get_client


class JSONFormatter(object):
  def __init__(self):
    self.client = get_client()

  def format_response(self, content: str) -> str:
    response = self.client.chat.completions.create(
      model="deepseek-ai/DeepSeek-V3",
      messages=[
        {
          "role": "system",
          "content": "You are a helpful assistant. You can make the json content more readable and concise.",
        },
        {
          "role": "user",
          "content": f"Please format the following json content: {content}",
        },
      ],
    )
    return response.choices[0].message.content or ""
