
'''
__init__ :Python的初始化方法
'''

class Enemy:
    def __init__(self):
        print("this is init ")

enemy1=Enemy()

print("---------")

'''
带参的构造方法
'''
class Enemy2:
    def __init__(self,x):
        self.energy=x
    def get_energy(self):
        print(self.energy)

jsaon=Enemy2(2)
sandy=Enemy2(18)
jsaon.get_energy()
sandy.get_energy()

