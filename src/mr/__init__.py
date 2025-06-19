# For meter reading location

from PIL import Image, ImageDraw
from pydantic import BaseModel

from mr.prompt import BasePrompt, MeterBoxPrompt, TextBoxPrompt
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
    result = self.read_image(image_path)

    # draw a rectangle on the image
    image = Image.open(image_path)

    # 获取图像尺寸并验证坐标
    img_width, img_height = image.size

    # 确保坐标在有效范围内
    left = max(0, min(result.output.top_left.x, img_width))
    top = max(0, min(result.output.top_left.y, img_height))
    right = max(0, min(result.output.bottom_right.x, img_width))
    bottom = max(0, min(result.output.bottom_right.y, img_height))

    # 确保裁剪区域有效
    if right <= left or bottom <= top:
      print("无效的裁剪区域")
      return

    cropped_image = image.crop((left, top, right, bottom))

    # write the cropped image to a file
    print(result.output)
    cropped_image.save(output_image_path)


if __name__ == "__main__":
  reader = MeterLocation()
  reader.show_image("resources/meter-2.jpg")
