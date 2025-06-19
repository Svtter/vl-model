import ast

from PIL import Image, ImageDraw, ImageFont


def plot_text_bounding_boxes(image_path, bounding_boxes, input_width, input_height):
  """
  Plots bounding boxes on an image with markers for each a name, using PIL, normalized coordinates, and different colors.

  Args:
      image_path: The path to the image file.
      bounding_boxes: A list of bounding boxes containing the name of the object
       and their positions in normalized [y1 x1 y2 x2] format.
  """

  # Load the image
  img = Image.open(image_path)
  width, height = img.size
  print(img.size)
  # Create a drawing object
  draw = ImageDraw.Draw(img)

  # Parsing out the markdown fencing
  bounding_boxes = parse_json(bounding_boxes)

  font = ImageFont.truetype("NotoSansCJK-Regular.ttc", size=10)

  # Iterate over the bounding boxes
  for i, bounding_box in enumerate(ast.literal_eval(bounding_boxes)):
    color = "green"

    # Convert normalized coordinates to absolute coordinates
    abs_y1 = int(bounding_box["bbox_2d"][1] / input_height * height)
    abs_x1 = int(bounding_box["bbox_2d"][0] / input_width * width)
    abs_y2 = int(bounding_box["bbox_2d"][3] / input_height * height)
    abs_x2 = int(bounding_box["bbox_2d"][2] / input_width * width)

    if abs_x1 > abs_x2:
      abs_x1, abs_x2 = abs_x2, abs_x1

    if abs_y1 > abs_y2:
      abs_y1, abs_y2 = abs_y2, abs_y1

    # Draw the bounding box
    draw.rectangle(((abs_x1, abs_y1), (abs_x2, abs_y2)), outline=color, width=1)

    # Draw the text
    if "text_content" in bounding_box:
      draw.text((abs_x1, abs_y2), bounding_box["text_content"], fill=color, font=font)

  # Display the image
  img.show()


def parse_json(json_output):
  # Parsing out the markdown fencing
  lines = json_output.splitlines()
  for i, line in enumerate(lines):
    if line == "```json":
      json_output = "\n".join(lines[i + 1 :])  # Remove everything before "```json"
      json_output = json_output.split("```")[0]  # Remove everything after the closing "```"
      break  # Exit the loop once "```json" is found
  return json_output
