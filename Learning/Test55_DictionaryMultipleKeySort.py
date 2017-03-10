'''
Dictionary Multiple Key Sort:字典多键排序
'''

from operator import itemgetter

users=[
    {'fname':'Bucky','lname':'Roberts'},
    {'fname':'Tom','lname':'Roberts'},
    {'fname':'Bernie','lname':'Zunks'},
    {'fname':'Jenna','lname':'Hayes'},
    {'fname':'Sally','lname':'Jones'},
    {'fname':'Amanda','lname':'Roberts'},
    {'fname':'Dean','lname':'Hayes'},
    {'fname':'C','lname':'A'}
]

for x in sorted(users,key=itemgetter('fname')):
    print(x)

print('-----')

for x in sorted(users,key=itemgetter('fname','lname')):
    print(x)