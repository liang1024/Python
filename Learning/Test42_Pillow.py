'''
Pillow：Python的Image库
'''

from PIL import Image

img=Image.open('57849d650ef11.jpg')
print(img.size)
print(img.format)

img.show()