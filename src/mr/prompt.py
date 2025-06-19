import abc


class BasePrompt(abc.ABC):
  @abc.abstractmethod
  def get_prompt(self) -> str:
    pass


class MeterBoxPrompt(BasePrompt):
  def get_prompt(self) -> str:
    prompt = """You are a helpful assistant that can read images and get the position of meter reading area.

    The image is a meter reading image. You need to identify the rectangular area that contains the meter reading digits/numbers.

    The meter reading area is the area that contains the actual meter reading display, typically where the numbers/digits are shown.

    Please identify the four corners of this reading area. Use the pillow coordinate system where the top left corner is (0, 0) and the bottom right corner is (image_width, image_height).

    Focus on the main reading display area, excluding any decorative elements, labels, or UI elements outside the core meter reading.
    """
    return prompt


class TextBoxPrompt(BasePrompt):
  def get_prompt(self) -> str:
    prompt = "Spotting all the text in the image with line-level, and output in JSON format."
    return prompt
