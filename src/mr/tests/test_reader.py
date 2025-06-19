from mr import MeterLocation


def test_reader():
  reader = MeterLocation()
  result = reader.read_image("resources/meter-2.jpg")
  print(result.output)
  print(result.usage())


if __name__ == "__main__":
  test_reader()
