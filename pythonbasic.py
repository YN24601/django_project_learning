# mystring = "Hello World"
# print(mystring[0:1])  
# print(mystring.upper())
# print(mystring.capitalize())
# list = mystring.split()
# print(list)
# print(f'{list[0]} my name is {list[1]}')

# list.append('New Item')
# list.insert(0, 'New Item')
# item_removed = list.pop()
# print(list)
# print(item_removed)
# list.pop(1)
# print(list)

# if 'Hello' in mystring:
#     print('Yes')
# else:
#     print('No')

# if 'Hello' in list:
#     print('Yes')
# else:
#     print('No')



# error and exceptions handling
# try:
#     print('Hello'+10)
# except TypeError as e:
#     print('Something went wrong')
#     print(e)
# else:
#     print('Nothing went wrong')
# finally:
#     print('This will run no matter what')

class Person:
    catgory = 'person'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old')

class Student(Person):
    catgory = 'student'
    def __init__(self, name, age, gpa):
        super().__init__(name, age)
        self.gpa = gpa
    def say_hello(self):
        print(f'Hello, my name is {self.name} and I am {self.age} years old and my gpa is {self.gpa}')
    def __str__(self):
        return f'Person(name={self.name}, age={self.age})'

"""
person = Person('John', 35)
person2 = Student(name='Jane', age=28, gpa=3.7)
print(person)
print(person2)
person.say_hello()
"""
