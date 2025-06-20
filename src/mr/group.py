"""LLM Model Groups"""

from pydantic import BaseModel


class ModelGroup(BaseModel):
  smart: str
  fast: str


openai_group = ModelGroup(
  smart="openai/gpt-4o",
  fast="openai/gpt-4o-mini",
)

deepseek_group = ModelGroup(
  smart="deepseek-ai/DeepSeek-V3",
  fast="deepseek-ai/DeepSeek-R1",
)


openrouter_group = ModelGroup(
  smart="openai/gpt-4o",
  fast="openai/gpt-4o-mini",
)

simsim_group = ModelGroup(
  smart="deepseek-ai/DeepSeek-V3",
  fast="deepseek-ai/DeepSeek-R1",
)
