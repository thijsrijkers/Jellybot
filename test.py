import praw
from PIL import Image
import requests
from io import BytesIO


url = "https://www.gettyimages.pt/gi-resources/images/Homepage/Hero/PT/PT_hero_42_153645159.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# getting colors
imgColor = Image.getcolors(img)

print(imgColor)