# For meter reading location

from pydantic import BaseModel

from mr.prompt import BasePrompt, MeterBoxPrompt
from vl_model.client import build_agent


class Point(BaseModel):
  x: float
  y: float


class LocationResposne(BaseModel):
  top_left: Point
  top_right: Point
  bottom_left: Point
  bottom_right: Point


class MeterLocation(object):
  def __init__(
    self,
    model_name: str = "openai/gpt-4o",
    prompt: BasePrompt = MeterBoxPrompt(),
  ):
    """
    初始化仪表读数定位器

    推荐的强大视觉模型：
    - anthropic/claude-3.5-sonnet (推荐，视觉能力最强)
    - anthropic/claude-3.5-haiku (快速且准确)
    - openai/gpt-4o (OpenAI最新模型)
    """
    self.agent = build_agent(model_name, LocationResposne)
    self.prompt = prompt.get_prompt()

  def read_image(self, image_path):
    result = self.agent.run_sync([self.prompt, image_path])
    return result

  def show_image(self, image_path, output_image_path: str = "./tmp/cropped_image.png"):
    """point out the meter reading area on the image"""
    from mr.clipper import Clipper

    result = self.read_image(image_path)
    result_json: LocationResposne = result.output  # type: ignore

    Clipper.clip(image_path, output_image_path, result_json)


if __name__ == "__main__":
  reader = MeterLocation()
  reader.show_image("resources/meter-2.jpg")
