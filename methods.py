from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO
import requests

image = Image.open("assets/img/brawl_stars_lobby.jpg")

def _change_font(size):
    font = ImageFont.truetype("assets/fonts/lilitaone-regular-webfont (2).ttf", size)
    return font

def _image_request(request):
    if request.status_code == 200:
        image = Image.open(BytesIO(request.content))
    return image

def profile(data):

    #Data
    icon_id = data['icon']['id']
    name = data['name']
    name_color = data['nameColor']
    tr = data['trophies']
    highest_tr = data['highestTrophies']
    exp = data['expPoints']
    level = data['expLevel']
    solo_win = data['soloVictories']
    duo_win = data['duoVictories']
    treevstree_win = data['3vs3Victories']
    best_robot_rumble_time = data['bestRoboRumbleTime']
    best_big_brawler_time = data['bestTimeAsBigBrawler']
    championship_challenge_win = data['isQualifiedFromChampionshipChallenge']
    brawlers = data['brawlers']

    #Icon
    icon_request = requests.get(f"https://cdn.brawlify.com/profile-icons/regular/{icon_id}.png")
    icon = _image_request(icon_request)
    image.paste(icon, (5, 5))

    #Name
    name_color = f"#{name_color[4:]}"
    imageDraw = ImageDraw.Draw(image)
    imageDraw.text((215, 0), name, font_size=100, fill=name_color, font=_change_font(100))

    return image

def error(response):
    imageDraw = ImageDraw.Draw(image)

    imageDraw.text((10, 10), f"Error: {str(response.status_code)}", font_size=100, font=_change_font(100))

    return image