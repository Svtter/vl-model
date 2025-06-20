from vl_model.client import get_client


class JSONFormatter(object):
  def __init__(self, response):
    self.client = get_client()
    self.response = response

  def format_response(self, content):
    response = self.client.chat.completions.create(
      model="gpt-4o-mini",
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
    return response.choices[0].message.content
