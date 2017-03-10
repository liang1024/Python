'''
Modes and Filters:模式和过滤器

'''

from PIL import Image
from PIL import ImageFilter

baby = Image.open('baby.jpg')
# 灰白色
black_white = baby.convert('L')
# 模糊
blur = baby.filter(ImageFilter.BLUR)
# 详细
detail = baby.filter(ImageFilter.DETAIL)
# 查找边缘
edges = baby.filter(ImageFilter.FIND_EDGES)

baby.show()
black_white.show()
blur.show()
detail.show()
edges.show()
