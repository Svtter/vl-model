from mr.clipper import Clipper
from mr.group import siliconflow_group
from mr.vlask import VlAsk


def test_read():
  vlask = VlAsk(siliconflow_group)
  img_path = "resources/meter-2.jpg"
  result = vlask.ask(img_path)

  output_path = f"./tmp/cropped_image_{(siliconflow_group.vision or "").replace('/', '_')}.png"
  Clipper.clip(img_path, output_path, result)
  print(f"Saved to {output_path}")


def test_ask_box():
  from mr.drawer import Drawer

  vlask = VlAsk(siliconflow_group)
  img_path = "resources/meter-2.jpg"
  result = vlask.ask_text_box(img_path)
  Drawer.draw_bounding_boxes(img_path, result.bounding_boxes, "./tmp/cropped_image_text_box.png")
