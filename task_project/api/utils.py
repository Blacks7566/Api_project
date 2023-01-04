from PIL import Image

def thumbnail_image(img):
    img = Image.open(img)
    thum = img.resize((200,300))
    return thum
    
def medium_image(img):
    img = Image.open(img)
    mid = img.resize((500,500))
    return mid
    
def large_image(img):
    img = Image.open(img)
    larg = img.resize((1028,786))
    return larg
    
def grayScale_image(img):
    img = Image.open(img)
    gray = img.convert('L')
    return gray