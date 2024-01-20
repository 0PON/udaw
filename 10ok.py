#class bald:
#    color = "Красный"
#    size= 42
#    def jump(self):
#        print(self.color, "мячик размера", str(self.size), "сделал прыг!")
#ok = bald()
#ok.jump()

class Human:
    name=""
    age=0
    height=5

    def __init__(self, ima, voz, rost ):
        self.name = ima
        self.age = voz
        self.height = rost

    def pn(self):
        print(self.name + " сделал бочку! Ему было "+str(self.age) +" годика!")

ok = Human("Михалыч", 3, 178)
ok.pn()