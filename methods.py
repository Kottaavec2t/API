from PIL import Image, ImageDraw
from io import BytesIO
import requests

image = Image.open("assets/img/brawl_stars_lobby.jpg")

def profile(data):

    icon_id = data['icon']['id']

    icon_request = requests.get(f"https://cdn.brawlify.com/profile-icons/regular/{icon_id}.png")
    if icon_request.status_code == 200:
        icon = Image.open(BytesIO(icon_request.content))

    name = data['name']
    name_color = data['nameColor']

    image.paste(icon, (5, 5))

    imageDraw = ImageDraw.Draw(image)
    imageDraw.text((215, 0), name, font_size=100, stroke_fill=name_color)

    return image

def error(response):
    imageDraw = ImageDraw.Draw(image)

    imageDraw.text((10, 10), f"Error: {str(response.status_code)}", font_size=100)

    return image