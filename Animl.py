class Animal:
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

print(Bob.voice())
print(Masha.voice())
print(Tony.voice())