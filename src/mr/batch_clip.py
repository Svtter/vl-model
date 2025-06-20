from mr import MeterLocation


def batch_agent_eval():
  for model_name in [
    "openai/gpt-4o",
    "anthropic/claude-3.5-sonnet",
    "google/gemini-2.5-pro",
  ]:
    reader = MeterLocation(model_name)
    file_name = f"./tmp/cropped_image_{model_name.replace('/', '_')}.png"
    reader.show_image("resources/meter-2.jpg", file_name)
    print(f"Saved to {file_name}")


if __name__ == "__main__":
  batch_agent_eval()
