class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.nunmber_od_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > 0 and new_floor <= self.nunmber_od_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('"Такого этажа не существует"')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(5)
h2.go_to(10)