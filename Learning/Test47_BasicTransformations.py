'''
 Basic Transformations:基本转换
 1.改变图片大小
 2.转换图片方向
 3。旋转90度
'''

from PIL import Image

baby = Image.open('baby.jpg')
sqaure_baby = baby.resize((250, 250))
flip_baby = baby.transpose(Image.FLIP_LEFT_RIGHT)
spin_baby = baby.transpose(Image.ROTATE_90)

baby.show()
sqaure_baby.show()
flip_baby.show()
spin_baby.show()
