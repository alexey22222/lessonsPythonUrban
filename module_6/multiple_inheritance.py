import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    def __init__(self, _cords = [0,0,0], speed = 0):
        self._cords = _cords
        self.speed = speed
    def move(self, dx, dy, dz):
        self._cords[0] = (self._cords[0] + dx) * self.speed
        self._cords[1] = (self._cords[1] + dy) * self.speed
        if (self._cords[2] + dz) < 0:
            print('It\'s toodeep, i can\'t dive:(' )
        else:
            self._cords[2] = (self._cords[2] + dz) * self.speed

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')
    def attack(self):
        if Animal._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif Animal._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")
    def speack(self):
        print(Animal.sound)
class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f'Here are(is) {random.randrange(1,5)} eggs for you')
class AquaticAnimal(Animal):
    Animal._DEGREE_OF_DANGER = 3
    def dive_in(self, dz):
        self.speed = self.speed / 2
        self._cords[2] = abs(self._cords[2] - dz * self.speed)
        pass
class PoisonousAnimal(Animal):
    Animal._DEGREE_OF_DANGER = 8

class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    def __init__(self, speed ):
        self.sound = "Click-click-click"
        Animal.sound = self.sound
        super().__init__(speed = speed)


db = Duckbill(10)
print(db.live)
print(db.beak)
db.speack()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

# print(Duckbill.mro())
