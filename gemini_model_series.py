from google import genai
from config.load_key import load_key

api_key = load_key("gemini", "api_key")
client = genai.Client(api_key=api_key)

for model in client.models.list():
    print(model.name, model.supported_actions)
