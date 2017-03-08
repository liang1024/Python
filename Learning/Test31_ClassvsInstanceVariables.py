
'''
类与实例变量
'''

class Girl:
    gender="female"
    def __init__(self,name):
        self.name=name

r=Girl("Rachel")
s=Girl("stanky")
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
