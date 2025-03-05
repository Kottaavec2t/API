from PIL import Image, ImageDraw

def profile(image, data):

    imageDraw = ImageDraw.Draw(image)
    
    imageDraw.text((10, 10), data['name'], font_size=100)

    #Save Image
    image.save(f"users/{data['tag']}.jpg")

    return image

def error(image, response):
    imageDraw = ImageDraw.Draw(image)

    imageDraw.text((10, 10), f"Error: {str(response.status_code)}", font_size=100)

    return image