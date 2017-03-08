'''
Flexible Number of Arguments:灵活的参数个数
'''

def add_numbers(*args):
    total=0
    for arg in args:
        total+=arg
    print(total)

add_numbers(1)
add_numbers(1,2)
add_numbers(1,2,3)
add_numbers(1,2,3,4,5,6,7,8,9,10)
