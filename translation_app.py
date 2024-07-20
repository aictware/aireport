from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.environ.get("API_KEY")
)

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    { "role": "system",
      "content": "You will be provided with a sentence in English, and your task is to translate it into Korean."
    },{
      "role": "user",
      "content": "My name is Jane. What is yours?"
    }
  ],
  temperature=0.7,
  max_tokens=64,
  top_p=1
)
print(response.choices[0].message.content)
