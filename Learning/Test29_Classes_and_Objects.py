
'''
class:Python的class对象
类的 def() 方法参数中自带self
'''
class Enemy:

    life=3

    def attack(self):
        print("ouch!")
        self.life-=1
    def checkLife(self):
        if self.life<=0:
            print("I am dead")
        else:
            print(str(self.life)+"life life")

enemy1=Enemy()
enemy2=Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checkLife()

enemy2.checkLife()