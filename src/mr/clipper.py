from PIL import Image

from mr import LocationResposne


class Clipper(object):
  @staticmethod
  def clip(image_path: str, output_image_path: str, location_response: LocationResposne):
    """
    clip the image by the location response
    """

    # draw a rectangle on the image
    image = Image.open(image_path)

    # 获取图像尺寸并验证坐标
    img_width, img_height = image.size

    # 确保坐标在有效范围内
    left = max(0, min(location_response.top_left.x, img_width))
    top = max(0, min(location_response.top_left.y, img_height))
    right = max(0, min(location_response.bottom_right.x, img_width))
    bottom = max(0, min(location_response.bottom_right.y, img_height))

    # 确保裁剪区域有效
    if right <= left or bottom <= top:
      print("无效的裁剪区域")
      return

    cropped_image = image.crop((left, top, right, bottom))

    # write the cropped image to a file
    cropped_image.save(output_image_path)
