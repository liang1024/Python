'''
剪裁图片
'''

from PIL import Image

img = Image.open("57849d650ef11.jpg")
area = (400, 400, 1200, 1000)

cropped_img = img.crop(area)

img.show()
cropped_img.show()
