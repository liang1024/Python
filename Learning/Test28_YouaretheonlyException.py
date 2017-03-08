
'''
Python中Exception的处理
例子：输入一个数字并进行除法运算
异常1：不是数字
异常2：不能除0
其他异常：结束
finally：必须执行
'''
while True:
    try:
        number =int(input("what's your fav number hoss?\n"))
        print(10/number)
        break
    except ValueError:
        print("Make sure and enter a number.")
    except ZeroDivisionError:
        print("Don't pick zero")
    except:
        break
    finally:
        print("loop complete")