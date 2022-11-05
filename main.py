# a class is like an object that stores functions an variables which  can be accessed thru the dot notaion

class Employee:
    def __init__(self, name):
        self.name = name

    def return_name(self):
        print(self)
        return self.name


# initializing a class
employee_one = Employee('fridah')
print(employee_one.return_name())
print(employee_one)
print(employee_one.__dict__)  # a list of attributes

# {ENCAPSULATION}
# We are setting and getting the atrributes using methods instead of setting and getting them directly


class MyClass:
    def __init__(self):
        print(
            'This method (__init__) is called everytime an instance of an object is created')

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age


zack = MyClass()
zack.setAge(45)
zack.getAge()
print(hasattr(zack, 'name'))
print(hasattr(zack, 'age'))

fruits = ['apple', 'oranges', 'bananas']
print(len(fruits))
print(fruits.__len__())

names = ['Rajesh', 'Rahul', 'Aarav', 'Sahil', 'Trevor']
for i, name in enumerate(names):
    print(f"Names number: {str(i)}")
    print(name)

# So, all animals show affections (show_affection), but they do differently.
# The “show_affection” behaviors is thus polymorphic in the sense that it acted differently
# depending on the animal. So, the abstract “animal” concept does not actually
# “show_affection”, but specific animals(like dogs and cats) have a concrete implementation of the action “show_affection”.


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eats {food}")


class Dog(Animal):
    def fetch(self, thing):
        print(f"{self.name} does after the {thing}")

    def show_affection(self):
        print(f"{self.name} wigs tail")


class Cat(Animal):
    def swatsstring(self):
        print(f"{self.name} shreds the string")

    def show_affection(self):
        print(f"{self.name} shows affection")


ranger = Dog('ranger')
ranger.eat('dog food')
ranger.fetch('thing')
ranger.show_affection()

# Overrinding


class Thought:
    def __init__(self):
        pass

    def message(self):
        print("Thought,always come and go")


class Advice(Thought):
    def __init__(self):
        super(Advice, self).__init__()

    def message(self):
        print('Warning: Risk is always involved when dealing with the market ')

# Inheriting the constructor


class MyAnimal:
    def __init__(self, name):
        self.name = name


class MyDog(MyAnimal):
    def __init__(self, name):
        super(MyDog, self).__init__(name)
        self.breed = 'Shepard'

    def fetch(self, thing):
        print(f"{self.name} goes after the {thing}")


d = MyDog('dogname')
print(d.name)
print(d.breed)

"""_summary_
{CLASS NOTES}
 Classes are preferred over modules because you can reuse them as they are and 
without much interference. While with modules, you have only one with the entire program
Objects are like Mini-imports
A class is like a mini-module and you can import in a similar way as you do for classes, 
using the concept called instantiate. Note that when you instantiate a class, you get an object.
class attributes are the attributes set inside the class while instance atributes are the atributes set
in the __init__ function
class data is the data that is shared by all the object instances
while instance data is unique to the instances
{INHERITANCE}
One of the major advantages of Object Oriented Programming is re-use. Inheritance is 
one of the mechanisms to achieve the same. Inheritance allows programmer to create a 
general or a base class first and then later extend it to more specialized class. It allows 
programmer to write better code.
Where X extends from Y. Y is the parent/super class while X is the child/sub class
Only data fields and method which are not private are accessible by child 
classes. Private data fields and methods are accessible only inside the class.
{ENCAPSULATION}
Making data or values private: hidding unnessecary information.
it also helps us use classes and objects without understanding the inner workings
Encapsulation provides us the mechanism of restricting the access to some of the object’s
components, this means that the internal representation of an object can’t be seen from 
outside of the object definition. Access to this data is typically achieved through special methods: Getters and Setters. 
{POLYMOPHISIM}
Polymorphism means many forms. That is, a thing or action is present in different forms
Polymorphism is an important feature of class definition in Python that is utilized when 
you have commonly named methods across classes or subclasses. This permits functions 
to use entities of different types at different times. So, it provides flexibility and loose 
coupling so that code can be extended and easily maintained over time.
It actually just means when a function or method produces different this because it depends on the input parameter
{ABSTRACTION}
Hiding all the unneccessary details

A class bundles together behavior{functions} and state{variables}
"""
