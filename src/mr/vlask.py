import base64

from mr import LocationResposne
from mr.group import ModelGroup, siliconflow_group
from mr.prompt import MeterBoxPrompt, TextBoxPrompt
from mr.text_location import TextLocationResponse
from mr.tools import JSONFormatter
from vl_model.client import get_client


class VlAsk(object):
  """用于使用不支持 tool 的模型，进行多轮对话。"""

  def __init__(self, model_group: ModelGroup):
    self.client = get_client()
    self.model_group = model_group

  def ask(self, image_path: str) -> LocationResposne:
    with open(image_path, "rb") as image_file:
      image_data = image_file.read()

    response = self.client.chat.completions.create(
      model=self.model_group.vision or "",
      messages=[
        {"role": "system", "content": MeterBoxPrompt().get_prompt()},
        {
          "role": "system",
          "content": f"The response should be in JSON format. The JSON schema should be: {LocationResposne.model_json_schema()}",
        },
        {
          "role": "user",
          "content": [
            {
              "type": "image_url",
              "image_url": {"url": f"data:image/jpeg;base64,{base64.b64encode(image_data).decode('utf-8')}"},
            }
          ],
        },
      ],
    )
    content = response.choices[0].message.content or ""
    json_formatter = JSONFormatter(group=self.model_group)
    content = json_formatter.format_response(content)
    if content:
      return LocationResposne.model_validate_json(content)
    else:
      raise ValueError("No content")

  def ask_text_box(self, image_path: str) -> TextLocationResponse:
    with open(image_path, "rb") as image_file:
      image_data = image_file.read()

    response = self.client.chat.completions.create(
      model=self.model_group.vision or "",
      messages=[
        {"role": "system", "content": TextBoxPrompt().get_prompt()},
        {
          "role": "system",
          "content": f"The response should be in JSON format. The JSON schema should be: {TextLocationResponse.model_json_schema()}",
        },
        {
          "role": "user",
          "content": [
            {
              "type": "image_url",
              "image_url": {"url": f"data:image/jpeg;base64,{base64.b64encode(image_data).decode('utf-8')}"},
            },
          ],
        },
      ],
    )
    content = response.choices[0].message.content or ""
    json_formatter = JSONFormatter(group=self.model_group)
    content = json_formatter.format_response(content)
    if content:
      return TextLocationResponse.model_validate_json(content)
    else:
      raise ValueError("No content")


if __name__ == "__main__":
  vlask = VlAsk(siliconflow_group)
  vlask.ask("./resources/meter-2.jpg")
