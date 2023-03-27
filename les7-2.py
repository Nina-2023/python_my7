from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_cloth_consumption(self):
        pass

class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def get_cloth_consumption(self):
        return self.size / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    @property
    def get_cloth_consumption(self):
        return 2 * self.height + 0.3

coat = Coat('Пальто', 50)
suit = Suit('Костюм', 180)

print(f'Расход ткани на пальто: {coat.get_cloth_consumption}')
print(f'Расход ткани на костюм: {suit.get_cloth_consumption}')

total_cloth_consumption = coat.get_cloth_consumption + suit.get_cloth_consumption
print(f'Общий расход ткани: {total_cloth_consumption}')