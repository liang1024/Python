
'''
Inheritance：继承
'''
class Parent:
    i=1
    def print_last_name(self):
        print("Roberts")

'''
Child继承于Parent，拥有父类的方法和属性
'''
class Child(Parent):
    def print_first_name(self):
        print("Bucky")
    # 重写之后将覆盖，不重写使用父类的方法
    # def print_last_name(self):
    #     print("Snitzleberg")

bucky=Child()
bucky.print_first_name()
bucky.print_last_name()
