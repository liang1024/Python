'''
Combine Images Together:将图像组合在一起
'''

from PIL import Image

cute=Image.open('cute.jpg')
landscape=Image.open('57849d650ef11.jpg')

area=(500,400,800,568)
landscape.paste(cute,area)

landscape.show()