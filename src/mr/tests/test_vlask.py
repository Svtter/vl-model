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
