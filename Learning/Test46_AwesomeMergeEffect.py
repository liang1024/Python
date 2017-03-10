'''
Awesome Merge Effect:很棒的合并效应
'''

from PIL import Image

landscape=Image.open('539bd63331668431.jpg')
cute=Image.open('landscape1.jpg')
r1,g1,b1=landscape.split()
r2,g2,b2=cute.split()

#  合并两张图片并展示
new_img=Image.merge("RGB",(r2,g1,b2))

new_img.show()