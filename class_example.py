# Just an example of the class

class Human:
    def __init__(self, name, length, nationality, age, job):
        self.name = name
        self.length = length
        self.nationality = nationality
        self.age = age
        self.job = job

hu1 = Human("Ahmed", "175 cm", "Egyption", "30 y", "programmer")
hu2 = Human("John", "166 cm", "American", "45 y", "pilot")
hu3 = Human("Adel", "203 cm", "Libyan", "19 y", "student")
hu4 = Human("Khaled", "186 cm", "Saudi", "32 y", "Teacher")

class Animal:
    def __init__(self, name, color, food):
        self.name = name
        self.color = color
        self.food = food

ani1 = Animal("Cat", "orange", "fish")
ani2 = Animal("Dog", "black", "bone")
ani3 = Animal("Monkey", "brown", "banana")

print(f"{hu1.name} with {hu1.age} love {ani1.name}")
print(f"{hu3.name} love {ani2.name} with {ani3.color} color")
print(f"{hu4.name} the {hu2.nationality} killed 20 {ani3.name}!!")
print(f"The {ani1.name} can't eat {ani2.name}s")