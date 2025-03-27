# from PIL import Image
#
# im = Image.open('photo.jpg')
#
# print(im.format, im.size, im.mode)
#
# out = im.resize((150, 190))
# # im.show()
#
# width, height = im.size
#
# print(dir(im))
# print(out.size)
# out.show()


from PIL import Image

# im = Image.open('photo.jpg')
#
# print(im.format, im.size, im.mode)
# w, h = im.size
#
# out = im.resize((w//2, h//2))
# print(out.size)
# out.show()

def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w //3, h //3))

im = new_photo('fon.jpg')
im2 = new_photo('photo.jpg')
print(im.size)

# im.paste(im2, (358, 175))


x_im = im.size[0] / 2  # 533.0
x_im2 = im2.size[0] / 2  # 175.0
x = int(x_im - x_im2)  # x = 358

y_im = im.size[1] / 2  # 400.0
y_im2 = im2.size[1] / 2  # 225.0
y= int(y_im - y_im2) # y = 175
# print(a, b)

im.paste(im2, (x, y))  # почему нельзя поставить переменную? потому, что в кортеже должен быть инт

im.show()