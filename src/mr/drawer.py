from PIL import Image, ImageDraw

from mr.text_location import BoundingBox


class Drawer:
  @staticmethod
  def draw_bounding_boxes(
    image_path: str,
    bounding_boxes: list[BoundingBox],
    output_image_path: str = "./tmp/cropped_image.png",
  ):
    """
    Draw bounding boxes on an image.
    """
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    for bounding_box in bounding_boxes:
      draw.rectangle(bounding_box.bbox_2d, outline="red", width=2)
    image.save(output_image_path)
