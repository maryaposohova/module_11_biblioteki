# Открытка для меня с помощью библиотеки pillow

import os
import sys
from PIL import Image
# from PIL.ImageDraw import ImageDraw
# from PIL.ImageFont import ImageFont
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
y = int(y_im - (y_im2+100))  # y = 175
# print(a, b)

im.paste(im2, (x, y))  # почему нельзя поставить переменную? потому, что в кортеже должен быть инт

try:
    Image.open('fon.jpg').verify()
    print("Изображение не повреждено")
except Exception as e:
    print(f"Ошибка в изображении: {e}")


draw = ImageDraw.Draw(im)
font = ImageFont.truetype('EkaterinaVelikayaOne.ttf', 101)
draw.text(xy=(x_im/4, y_im+40), text='Мне можно все, что я хочу', fill='black', font=font)
font = ImageFont.truetype('EkaterinaVelikayaOne.ttf', 100)
draw.text(xy=(x_im/4, y_im+40), text='Мне можно все, что я хочу', fill='white', font=font)


help(draw.text)  # все параметры текста

#  # Если временный файл не открывается через im.show(), то:
im.save('result.jpg')
os.startfile('result.jpg')
# im.show()
