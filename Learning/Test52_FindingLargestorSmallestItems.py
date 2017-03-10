'''
Finding Largest or Smallest Items:  发现最大或最小的Items
'''
import heapq

grades=[32,43,654,34,132,66,99,532]
# 找出3个最大的Item
print(heapq.nlargest(3,grades))

stocks=[
    {'ticker':'AAPL','price':200},
    {'ticker':'GOOD','price':800},
    {'ticker':'F','price':54},
    {'ticker':'MSFT','price':313},
    {'ticker':'TUNA','price':68},
]
# 找出最小的2个  参数：个数，被迭代Object，key=value：被比较的
print(heapq.nsmallest(2,stocks,key=lambda stock:stock['price']) )
