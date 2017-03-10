'''
Getting Individual Channels:分解一张图片，得到R G B不同样式的图片
'''

from PIL import Image

cute=Image.open('cute.jpg')
r,g,b=cute.split()

r.show()
g.show()
b.show()