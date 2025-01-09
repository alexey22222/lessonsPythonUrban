class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        House.houses_history.append(args[0])
        return object.__new__(cls)
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_od_floors = number_of_floors
    def go_to(self, new_floor):
        if new_floor > 0 and new_floor <= self.number_od_floors:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('"Такого этажа не существует"')
    def __len__(self):
        return  self.number_od_floors
    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_od_floors}'
    def __eq__(self, other):
        return self.number_od_floors == other
    def __le__(self, other):
        return self.number_od_floors <= other
    def __lt__(self, other):
        return self.number_od_floors < other
    def __gt__(self, other):
        return self.number_od_floors > other
    def __ge__(self,other):
        return self.number_od_floors >= other
    def __ne__(self, other):
        return self.number_od_floors != other
    def __add__(self, value):
        # if isinstance(value.int):
        self.number_od_floors += value
        return House(self.name, self.number_od_floors)
    def __radd__(self, other):
        self.__add__(other)
        return House(self.name, self.number_od_floors)
    def __iadd__(self, other):
        self.__add__(other)
        return House(self.name, self.number_od_floors)
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории' )

if __name__ == '__main__':
    h1 = House('ЖК Эльбрус', 10)
    print(House.houses_history)
    h2 = House('ЖК Акация', 20)
    print(House.houses_history)
    h3 = House('ЖК Матрёшки', 20)
    print(House.houses_history)
    # Удаление объектов
    del h2
    del h3
    print(House.houses_history)
