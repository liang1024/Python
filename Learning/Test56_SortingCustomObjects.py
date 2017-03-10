'''
Sorting Custom Objects:对自定义对象进行排序
'''

from operator import attrgetter

class User:

    def __init__(self ,name,user_id):
        self.name=name
        self.user_id=user_id

    def __repr__(self):
        return self.name+":"+str(self.user_id)

users=[
    User('Bucky',43),
    User('Sally',5),
    User('Tuna',61),
    User('Brian',2),
    User('Joby',77),
    User('Amanda',9),
]
# 遍历输出
for user in users:
    print(user)

print('-----')
# 按名字排序
for name in sorted(users,key=attrgetter('name')):
    print(name)

print('-----')
# 按照user_id排序
for user_id in sorted(users,key=attrgetter('user_id')):
    print(user_id)


