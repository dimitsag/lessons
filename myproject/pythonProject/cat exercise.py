class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


cat1 = Cat("Cap", 100)
cat2 = Cat("bucky", 110)
cat3 = Cat("Tony", 50)


def cat_age(*age):
    return max(age)


print(f"the oldest cat is {cat_age(cat1.age, cat2.age, cat3.age)} years old")


class Pets:
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Mitsos(Cat):
    def sing(self, sounds):
        return f"{sounds}"


my_cats = [Mitsos("Mitsos", 16), Sally("Sally", 14),
           Simon("Simon", 10)]
# cat1 = Simon("Simon", 10)
# cat2 = Sally("Sally", 14)
# cat3 = Mitsos("Mitsos", 16)
#
# my_cats.append(cat1)
# my_cats.append(cat2)
# my_cats.append(cat3)

my_pets = Pets(my_cats)

my_pets.walk()
