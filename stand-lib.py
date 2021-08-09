from random import randint, choice
print(randint(1,10))

players = ['nv','ad','nw','st']
random_pick = choice(players)
print(random_pick)

from PIL import Image, ImageFilter

im= Image.open('test.jpg')
im2=im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')