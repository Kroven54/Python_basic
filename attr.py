class Animal:
    numInstances = 0

    @staticmethod
    def print_num_instances():
        print(f'Кол-во созданных сущностей {Animal.numInstances}')


    def __init__(self):
        Animal.numInstances = Animal.numInstances + 1

    def voice(self):
        return 'Some voice'


class Dog(Animal):
    def voice(self):
        return 'Woof'


class Cat(Animal):
    def voice(self):
        return 'Meow'


class Hamster(Animal):
    def voice(self):
        return 'Squeak'


Bob = Dog()
Masha = Cat()
Tony = Hamster()
Animal.print_num_instances()
print(Bob.voice())
print(Masha.voice())
print(Tony.voice())
