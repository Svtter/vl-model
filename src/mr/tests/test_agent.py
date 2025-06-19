from pydantic import BaseModel

from vl_model.client import build_agent


class CityLocation(BaseModel):
  city: str
  country: str


def test_agent():
  agent = build_agent("google/gemini-flash-1.5-8b", CityLocation)
  result = agent.run_sync("Where were the olympics held in 2012?")
  print(result.output)
  # > city='London' country='United Kingdom'
  print(result.usage())
  # > Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65)


if __name__ == "__main__":
  test_agent()
