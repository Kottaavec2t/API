from PIL import Image, ImageDraw, ImageFont, ImageColor
from io import BytesIO
import requests
import API_KEY

image = Image.open("assets/img/brawl_stars_lobby.jpg")
imageDraw = ImageDraw.Draw(image)

display_trophies = Image.open("assets/img/display_trophies_bar.png")
display_max_trophies = Image.open("assets/img/display_max_trophies_bar.png")
display_level = Image.open("assets/img/display_level_bar.png")
display_solo_win = Image.open("assets/img/display_solo_win_bar.png")
display_duo_win = Image.open("assets/img/display_duo_win_bar.png")
display_trio_win = Image.open("assets/img/display_trio_win_bar.png")
display_brawlers = Image.open("assets/img/display_brawlers_count_bar.png")

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
    trio_win = data['3vs3Victories']
    best_robot_rumble_time = data['bestRoboRumbleTime']
    best_big_brawler_time = data['bestTimeAsBigBrawler']
    championship_challenge_win = data['isQualifiedFromChampionshipChallenge']
    brawlers = data['brawlers']

    #All Brawlers Request
    headers = {
        "Authorization": f"Bearer {API_KEY.API_KEY}",
        "Accept": "application/json"
    }
    all_brawlers_request = requests.api.get("https://api.brawlstars.com/v1/brawlers", headers=headers)
    all_brawlers_data = all_brawlers_request.json()
    all_brawlers = all_brawlers_data['items']

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

    #Level
    image.paste(display_level, (-60, -235), mask=display_level)
    imageDraw.text((320, 130), str(level), fill="black", font=_change_font(50))

    #Solo Win
    image.paste(display_solo_win, (725, -335), mask=display_solo_win)
    imageDraw.text((1060, 25), str(solo_win), fill="black", font=_change_font(50))
    
    #Duo Win
    image.paste(display_duo_win, (725, -230), mask=display_duo_win)
    imageDraw.text((1060, 130), str(duo_win), fill="black", font=_change_font(50))

    #Trio Win
    image.paste(display_trio_win, (1125, -335), mask=display_trio_win)
    imageDraw.text((1460, 25), str(trio_win), fill="black", font=_change_font(50))
    
    #Brawlers
    total_brawler_count = 0
    brawler_count = 0
    for brawler in all_brawlers:
        total_brawler_count += 1
    for brawler in brawlers:
        brawler_count += 1
    image.paste(display_brawlers, (1125, -230), mask=display_brawlers)
    imageDraw.text((1460, 130), f"{str(brawler_count)}/{str(total_brawler_count)}", fill="black", font=_change_font(50))

    return image

def error(response):

    imageDraw.text((10, 10), f"Error: {str(response.status_code)}", font_size=100, font=_change_font(100))

    return image