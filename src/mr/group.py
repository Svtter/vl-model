"""LLM Model Groups"""

from typing import Optional

from pydantic import BaseModel


class ModelGroup(BaseModel):
  smart: str
  fast: str
  reasoner: str
  vision: Optional[str] = None


openai_group = ModelGroup(
  smart="openai/gpt-4o",
  fast="openai/gpt-4o-mini",
  reasoner="openai/o1-mini",
  vision="openai/gpt-4o-vision-preview",
)

deepseek_group = ModelGroup(
  smart="deepseek/deepseek-reasoner",
  fast="deepseek/deepseek-chat",
  reasoner="deepseek/deepseek-reasoner",
)


openrouter_group = ModelGroup(
  smart="openai/gpt-4o",
  fast="openai/gpt-4o-mini",
  reasoner="openai/o1-mini",
  vision="openai/gpt-4o-vision-preview",
)

siliconflow_group = ModelGroup(
  smart="deepseek-ai/DeepSeek-R1",
  fast="deepseek-ai/DeepSeek-V3",
  reasoner="deepseek-ai/DeepSeek-R1",
  vision="Qwen/Qwen2.5-VL-72B-Instruct",
)


def get_group() -> ModelGroup:
  """get current provider group"""
  from mr.conf import main_provider

  if main_provider == "openrouter":
    return openrouter_group
  elif main_provider == "siliconflow":
    return siliconflow_group
  else:
    raise ValueError(f"Invalid main provider: {main_provider}")
