import openai
from PIL import Image
import requests
from io import BytesIO


openai.api_key = 'API-KEY'

response = openai.Image.create(
    prompt='TEXT',
    n=1,
    size='1024x1024'
)

image_url = response['data'][0]['url']
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img.save('photo.jpg')
photo = open('photo.jpg', 'rb')
