import yaml


class Animal:
    def __init__(self,name,color,age,gender):
        self.name=name
        self.color=color
        self.age=age
        self.gender=gender

    def running(self):
        print("I can run")

    def cry(self):
        print("I can cry")

class cat(Animal):
    def __init__(self,name,color,age,gender):
        super().__init__(name,color,age,gender)
        self.hair='short hair'

    def cry(self):
        print("miaow miaow")

    def skills(self,skill):
        if skill == True:
            return "I can catch mouses"
        else:
            return "I can't catch mouses"

class dog(Animal):
    def __init__(self, name, color, age, gender):
        super().__init__(name, color, age, gender)
        self.hair = 'long hair'

    def cry(self):
        print("woof woof")

    def skills(self,skill):
        if skill == True:
            return "I can look after the house"
        else:
            return "I can't look after the house"

if __name__ == '__main__':

    with open("AnimalInfo.yml") as a:
        animal=yaml.safe_load(a)

    kitty=cat(animal['cat']['name'],animal['cat']['color'],animal['cat']['age'],animal['cat']['gender'])
    kitty.skills(True)
    print(f"My name is {kitty.name}, I'm a {kitty.color} {kitty.hair} cat, I'm {kitty.age} years old,"
          f"my gender is {kitty.gender}. And {kitty.skills(True)}.")

    Husky=dog(animal['dog']['name'],animal['dog']['color'],animal['dog']['age'],animal['dog']['gender'])
    Husky.skills(True)
    print(f"My name is {Husky.name}, I'm a {Husky.color} {Husky.hair} cat, I'm {Husky.age} years old,"
          f"my gender is {Husky.gender}. And {Husky.skills(True)}.")