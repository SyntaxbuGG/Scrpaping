from uuid import uuid1
# class Person:
#     pass
#     def __init__(self, first_name,last_name,age,birth_date,where_born):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age=age
#         self.birth_date=birth_date
#         self.where_born=where_born
#     def __repr__(self):
#         return f"{self.first_name},{self.last_name}"
#
# Abbos = Person("Abbos","Zarbotbekov",23,2000,"Andijan")
# print(Abbos)
#
# class Subjects:
#     def __init__(self,title):
#         self.title=title
#     def __repr__(self):
#         return f"{self.title}"
#
# subject1 = Subjects("math")
# subject=Subjects("computer science")
#
# # #
# #
class Teacher:
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.course=1

#
#
#
#         self.subjects=[]
#     def add_subject(self,Subs):
#         self.subjects.append(Subs)
#
#     def subject_1(self):
#         return self.subjects
#
#
#
#
#
#     def __repr__(self):
#         return f" {self.first_name} {self.last_name}"
# techer=Teacher("Zoya","Alexandrova",)
#
# techer.add_subject(subject)
# techer.add_subject(subject1)
# print(techer.subject_1())

# #
#

#

# class Person:
#     person_count = 1
#
#     def __init__(self, first_name, last_name, age, birth_date, where_born):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.birth_date = birth_date
#         self.where_born = where_born
#         self.person_count += 1
#
#     def get_fullname(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def __repr__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def get_age(self):
#         return self.age
#
#
# person = Person('Alisher', 'Alisherov', 40, 1983, 'Tashkent, Uzbekistan')
# person1 = Person('Javohir', 'Qodirov', 23, 2000, 'Fergana, Uzbekistan')
# print(person.get_fullname())


# class Dog:
#     def send_bark(self):
#         print("Woof! I'm gonna bite you")
#
# dog = Dog()
# dog.send_bark()
# Dog.send_bark(dog)

# class Slojenie:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def calc_cum(self):
#         return self.a+self.b
#
# sloj=Slojenie(5,9)
# print(sloj.calc_cum())

# class People :
#     def __init__(self,degree,first_name,last_name):
#         self.degree=degree
#         self.firstname=first_name
#         self.last_name=last_name
#         self.subjects=[]
#         self.age = None
#     def add_suject(self,title):
#         self.subjects.append(title)
#     def __repr__(self):
#         return f'{self.degree} {self.firstname} {self.last_name} {self.subjects} {self.age}'
#
# class Subject:
#     def __init__(self,math,geometr,reading):
#         self.math=math
#         self.geometr=geometr
#         self.reading=reading
#
#     def __repr__(self):
#         return f"{self.math},{self.geometr},{self.reading}"
#
# subject1=Subject("mathematic","geometr","reading")
# print(subject1)
#
# People1=People("Teacher","Zoya","seergeeva")
# People1.add_suject(subject1)
# print(People1.__dict__)
# #
# import random
# class User:
#     def __init__(self,ism,nick,email):
#         self.ism=ism
#         self.nick=nick
#         self.email=email
#     def upnick(self):
#         return self.ism.capitalize()
#
#     def get_info(self):
#         return f"Foy ismi:{self.upnick()} \n uning niki : {self.nick} \n uning email: {self.email}"
# user1=User("abbos","abo","zarbotbekovabbosbek@gmail.com")
# print(user1.get_info())
# print(user1.__dict__)


# class Human:
#     group="P16"
#     def __new__(cls, *args, **kwargs):
#         print(f"Creating the {cls.__name__} ")
#         obj=object.__new__(cls)
#         obj.degree="Math"
#         return obj
#     def __init__(self,first_name,last_name):
#         print("init")
#         self.first_name=first_name
#         self.last_name=last_name
#
#
#     @staticmethod
#     def to_upper(text):
#         return text.upper()
#
#     @staticmethod
#     def to_title(text):
#         return text.tittle()
#
#
#     @classmethod
#     def update_group(cls,group_name):
#         cls.group=group_name
#
#
#     def del_1(self):
#         del self
#
#
#     def d
#
#
#
#
#
#
# student=Human("Abbos","Zarbotbekov")
# student1=Human("Ulubkek","Karimov")
# print(student.__dict__)
# print(student.group)
# Human.group="P12"
# print(student.to_upper("abbos"))
# print(student1.group)
# print(student.group)
# print(len(student.__dict__))