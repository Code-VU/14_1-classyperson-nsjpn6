'''
Starter code!
don't forget the use of 'self' and to have the methods:
1. __init__
2. increase_age
3. say_greeting
4. count_to_age
'''

class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def increase_age(self):
        self.age = self.age + 1
        print(self.age)
        return ""

    def say_greeting(self):
        print(f"Hello world! My name is {self.name}!")
        return ""

    def count_to_age(self):
        for year in range(1, self.age+1):
            print(year)
        return ""


nathan = Person(32, "Nathan")

print(nathan.age)
print(nathan.say_greeting())
print(nathan.increase_age())
print(nathan.count_to_age())



    






# You won't need to call anything here.