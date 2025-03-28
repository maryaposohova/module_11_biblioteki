import os
import sys
from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL.ImageFont import ImageFont
from PIL import ImageDraw, ImageFont
def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w // 2, h // 2))


im = new_photo('fon.jpg')
im2 = new_photo('photo.jpg')
print(im.size)
print(sys.path)
# im.paste(im2, (358, 175))


x_im = im.size[0] / 2  # 533.0
x_im2 = im2.size[0] / 2  # 175.0
x = int(x_im - x_im2)  # x = 358

y_im = im.size[1] / 2  # 400.0
y_im2 = im2.size[1] / 2  # 225.0
y= int(y_im - y_im2) # y = 175
# print(a, b)

im.paste(im2, (x, y))  # почему нельзя поставить переменную? потому, что в кортеже должен быть инт



try:
    Image.open('fon.jpg').verify()
    print("Изображение не повреждено")
except Exception as e:
    print(f"Ошибка в изображении: {e}")
im.save('result.jpg')

draw = ImageDraw.Draw(im)
font = ImageFont.truetype('EkaterinaVelikayaOne.ttf', 15)
draw.text(xy=(0, 0), text='Мне можно все, что я хочу', fill='green')


help(draw.text)  # все параметры текста

# # ecли временный файл не открывается через im.show(), то:

os.startfile('result.jpg')
# im.show()



