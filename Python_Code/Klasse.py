class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f"{self.name} ist {self.age} Jahre alt."

# Beispiel für die Verwendung der Klasse
person1 = Person("Max", 25)
print(person1.get_info())