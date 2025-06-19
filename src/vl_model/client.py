import os
import typing as t

import openai
from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openrouter import OpenRouterProvider

load_dotenv(find_dotenv())


class Client(object):
  def __init__(self):
    self.client = openai.OpenAI(
      api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("OPENAI_BASE_URL")
    )
    self.async_client = openai.AsyncOpenAI(
      api_key=os.getenv("OPENAI_API_KEY"), base_url=os.getenv("OPENAI_BASE_URL")
    )

  def build_model(self, model_name: str):
    model = OpenAIModel(
      model_name,
      provider=OpenRouterProvider(api_key=os.getenv("OPENROUTER_API_KEY") or ""),
    )
    return model

  def build_agent(self, model_name: str, output_type: t.Type[BaseModel]):
    """build openrouter model and agent for pydantic-ai"""
    agent = Agent(self.build_model(model_name), output_type=output_type)
    return agent


client = Client()


def get_client():
  return client.client


def get_async_client():
  return client.async_client


def build_agent(model_name: str, output_type: t.Type[BaseModel]):
  return client.build_agent(model_name, output_type)


def build_model(model_name: str):
  return client.build_model(model_name)
