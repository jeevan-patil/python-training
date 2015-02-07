#!/usr/bin/python3

class AnimalActions:
    def quack(self): return self.actions['quack']
    def feathers(self): return self.actions['feathers']
    def bark(self): return self.actions['bark']
    def fur(self): return self.actions['fur']

class Duck(AnimalActions):
    actions = dict(
        quack = "Quaak!",
        feathers = "The duck has white and grey feathers.",
        bark = "The duck cannot bark.",
        fur = "The duck has no fur."
    )

class Person(AnimalActions):
    actions = dict(
        quack = "The person imitates a duck.",
        feathers = "A person takes a feather from the ground and shows it.",
        bark = "The person says woof!",
        fur = "The person puts on a fur coat."
    )

class Dog(AnimalActions):
    actions = dict(
        quack = "The dog can not quack.",
        feathers = "The dog has no feathers.",
        bark = "Arf!",
        fur = "The dog has white fur with black spots."
    )

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())

def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print('In the forest:')
    for o in (donald, john, fido):
        in_the_forest(o)

    print('In the dog house:')
    for o in (donald, john, fido):
        in_the_doghouse(o)

if __name__ == "__main__" : main()
