from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO
import requests

image = Image.open("assets/img/brawl_stars_lobby.jpg")
imageDraw = ImageDraw.Draw(image)

display_trophies = Image.open("assets/img/display_trophies_bar.png")
display_max_trophies = Image.open("assets/img/display_max_trophies_bar.png")
display_level = Image.open("assets/img/display_level_bar.png")

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
    trophies = data['trophies']
    highest_trophies = data['highestTrophies']
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
    imageDraw.text((215, 0), name, fill=name_color, font=_change_font(100))

    #Trophies
    image.paste(display_trophies, (325, -335), mask=display_trophies)
    imageDraw.text((660, 25), str(trophies), fill="black", font=_change_font(50))

    #Max Trophies
    image.paste(display_max_trophies, (325, -230), mask=display_max_trophies)
    imageDraw.text((660, 130), str(highest_trophies), fill="black", font=_change_font(50))

    #Max Trophies
    image.paste(display_level, (-60, -235), mask=display_level)
    imageDraw.text((320, 130), str(level), fill="black", font=_change_font(50))


    return image

def error(response):

    imageDraw.text((10, 10), f"Error: {str(response.status_code)}", font_size=100, font=_change_font(100))

    return image