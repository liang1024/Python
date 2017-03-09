'''
Unpack List or Tuples:打开列表或元组
'''

# 变量tuples
item=['December 23,2015 ','Bread Gloves',8.51]
print(item)
print("-----------------")

# 接收tuples
date,name,price=['December 23,2015 ','Bread Gloves',8.51]
print(name)
print("-----------------")

# 截取中间并求平均值
def drop_first_last(grades):
    first,*middle,last=grades
    avg=sum(middle)/len(middle)
    print(avg)

#
drop_first_last([65,76,98,54,21])
#
drop_first_last([65,76,98,54,21,54,65,99,88,78])
