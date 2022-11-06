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

#Method overriding

class Parent:
    def __init__(self):
        self.value = 4
    
    def get_value(self):
        return self.value


class Child(Parent):
    def get_value(self):
        return self.value + 1

#How to use the super() method

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width  = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (2 * self.length) + (2 * self.width)

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self,length):
        super().__init__(length,length)


class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6
    
    def volume(self):
        face_area = super().area()
        return face_area * self.area

# super(Square,self).__init__(length,length) is equivalent to super().__init__(length,length)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class RightPyramid(Triangle, Square):
    def __init__(self, base, slant_height):
        self.base = base
        self.slant_height = slant_height

    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area


#Singleton Example
#In the below example Logger is a Singleton
""" 
When __new__ is called, it normally constructs a new instance of that class. When we 
override it, we first check if our singleton instance has been created or not. If not, we 
create it using a super call. Thus, whenever we call the constructor on Logger, we always get the exact same instance.
"""
class Logger:
    def __new__(cls, *args, **kwargs):
        # checking if the class has an attribute called _logger
        # if it does not we add it
        if not hasattr(cls, '_logger'):
             cls._logger = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._logger



"""
(HOW TO ADD METHODS IN DJANGO MODELS)

(RESIZING THE UPLOADED IMAGE BEFORE SAVING IT TO THE DATABASE)

from django.conf import settings
from django.db import models
from PIL import Image

class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (800, 800)
    
    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)
        
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

(GETING THE WORD COUNT OF THE BLOG CONTENT)

class Blog(models.Model):
    photo = models.ForeignKey(Photo, null=True, on_delete=models.SET_NULL, blank=True)
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    starred = models.BooleanField(default=False)
    word_count = models.IntegerField(null=True)

    def _get_word_count(self):
        return len(self.content.split(' '))

    def save(self, *args, **kwargs):
        self.word_count = self._get_word_count()
        super().save(*args, **kwargs)


(SAVING THE SLUG FIELD WITH THE TITLE BEFORE SAVING THE METHOD IN THE DATABASE)

from django.db import models

# importing slugify from django
from django.utils.text import slugify

# Create your models here.
class GeeksModel(models.Model):
	title = models.CharField(max_length = 200)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(GeeksModel, self).save(*args, **kwargs)


"""


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

{OVERIDING}
Overriding is a very important part of OOP since it makes inheritance utilize its full power. 
By using method overriding a class may "copy" another class, avoiding duplicated code, 
and at the same time enhance or customize part of it.
Method overriding is thus a part of the inheritance mechanism.
In Python method overriding occurs by simply defining in the child class  a method with the same name of 
a method in the parent class. When you  define a method in the object you make this latter able to satisfy
that  method call, so the implementations of its ancestors do not come in  play.


"""
