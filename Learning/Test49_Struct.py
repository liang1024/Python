'''
struct：结构
'''

from struct import *

 # store as bytes data

# 打包(格式，打包的数据)
packed_data=pack('iif',6,19,4.73)
#
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# Unpack:解包(格式，打包的数据)
original_data=unpack('iif',packed_data)
print(original_data)