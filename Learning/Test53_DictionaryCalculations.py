'''
Dictionary Calculations:字典的计算
'''

stocks={
    'GOOD':434,
    'AAPL':325,
    'FB':54,
    'AMZN':623,
    'F':32,
    'MSFT':549,
    }
# 错误
# print(min(stocks))

# 使用zip将value放在前，通过min进行排序选出最低的价格
min_price=min(zip(stocks.values(),stocks.keys()))
print(min_price)