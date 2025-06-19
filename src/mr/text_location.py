from PIL import Image, ImageDraw
from pydantic import BaseModel

from mr.prompt import TextBoxPrompt
from vl_model.client import build_agent


class BoundingBox(BaseModel):
  """
  {
  "bbox_2d": [125, 169, 754, 208], "text_content": "UNIHAKKA INTERNATIONAL SDN BHD",
  },
  """

  bbox_2d: list[int]
  text_content: str


class TextLocationResponse(BaseModel):
  bounding_boxes: list[BoundingBox]


class TextLocation(object):
  def __init__(
    self,
    model_name: str = "openai/gpt-4o",
  ):
    self.agent = build_agent(model_name, TextLocationResponse)
    self.prompt = TextBoxPrompt().get_prompt()

  def read_image(self, image_path):
    result = self.agent.run_sync([self.prompt, image_path])
    return result

  def show_image(self, image_path, output_image_path: str = "./tmp/cropped_image.png"):
    result = self.read_image(image_path)
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    bounding_boxes: list[BoundingBox] = result.output.bounding_boxes

    for bounding_box in bounding_boxes:
      draw.rectangle(bounding_box.bbox_2d, outline="red", width=2)

    image.save(output_image_path)
