'''
Dictionary:拥有key与value,以键值对形式存储
'''
classmates = {"Tony": 'cool but smells', "Emma": "sits behind me", "lucy": 'asks to many questions'}

print(classmates["Tony"])
print("-----------")

for k, v in classmates.items():
    print(k + v)
