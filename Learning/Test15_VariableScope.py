a=7823

def corn():
    #  局部变量不可以供其他变量使用
    # a = 7823
    print(a)


def fudge():
    print(a)


corn()
fudge()