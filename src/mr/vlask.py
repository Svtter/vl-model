import base64

from openai.types.shared_params import ResponseFormatJSONSchema
from openai.types.shared_params.response_format_json_schema import JSONSchema

from mr import LocationResposne
from mr.prompt import MeterBoxPrompt
from vl_model.client import get_client


class VlAsk(object):
  """用于使用不支持 tool 的模型，进行多轮对话。"""

  def __init__(self, model_name: str):
    self.client = get_client()
    self.model_name = model_name

  def ask(self, image_path: str) -> LocationResposne:
    with open(image_path, "rb") as image_file:
      image_data = image_file.read()

    response = self.client.chat.completions.create(
      model=self.model_name,
      messages=[
        {"role": "system", "content": MeterBoxPrompt().get_prompt()},
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
      response_format=ResponseFormatJSONSchema(
        json_schema=JSONSchema(
          schema=LocationResposne.model_json_schema(),
          name="location",
          description="location of meter reading area",
        ),
        type="json_schema",
      ),
    )
    content = response.choices[0].message.content or ""
    if content:
      return LocationResposne.model_validate_json(content)
    else:
      raise ValueError("No content")


if __name__ == "__main__":
  vlask = VlAsk("Qwen/Qwen2.5-VL-72B-Instruct")
  vlask.ask("./resources/meter-2.jpg")
