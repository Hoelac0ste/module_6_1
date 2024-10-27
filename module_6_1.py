class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, plant):
        if plant.edible == True:
            print(f'{self.name} съел {plant.name}')
            self.fed = True
        else:
            self.alive = False
            print(f'{self.name} не стал есть {plant.name}')

class Plant:
    def __init__(self, name, edible = False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    pass
class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    pass

p1 = Fruit('Апельсин', edible = True)
p2 = Flower('Лапух')
a1 = Predator('Медведь Балу')
a2 = Mammal('Капибара')
a2.eat(p1)
a2.eat(p2)
a1.eat(p2)


