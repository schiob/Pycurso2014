class Pikachu():
    def __init__(self, hp, lvl, str):
        self.hp = hp
        self.lvl = lvl
        self.str = str

    def attack(self, enemigo):
        enemigo.hp = enemigo.hp - self.str
        
class Charmander():
    def __init__(self, hp, lvl, str):
        self.hp = hp
        self.lvl = lvl
        self.str = str

    def attack(self, enemigo):
        enemigo.hp -= self.str

pikachu_Ash = Pikachu(300, 100, 50)
charmander_Luis = Charmander(70, 5, 32)

flag = True

while pikachu_Ash.hp > 0 and charmander_Luis.hp > 0:
    if flag:
        pikachu_Ash.attack(charmander_Luis)
        flag = False
    else:
        charmander_Luis.attack(pikachu_Ash)
        flag = True

if pikachu_Ash.hp > 0:
    print('gano pikachu')
else:
    print('gano charmander')
