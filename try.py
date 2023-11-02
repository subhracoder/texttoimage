import os
import openai

from config import key

openai.api_key = key

response = openai.Image.create(
  prompt="play",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
