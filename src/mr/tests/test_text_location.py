from mr.text_location import TextLocation


def test_text_location():
  text_location = TextLocation()
  result = text_location.read_image("resources/meter-2.jpg")
  print(result)
  text_location.show_image("resources/meter-2.jpg")
