# # # # class Counter:
# # # #     count=0
# # # #     def __init__(self,operator):
# # # #
# # # #         self.operator = operator
# # # #
# # # #     def increment(self):
# # # #         self.count += 1
# # # #         return self.count
# # # #
# # # #     def dicrement(self):
# # # #         self.count -= 1
# # # #         return self.count
# # # #
# # # #
# # # #
# # # #     def getinfo(self):
# # # #         if self.operator =='+':
# # # #
# # # #             return self.increment()
# # # #         elif self.operator == '-':
# # # #
# # # #             return self.dicrement()
# # # #         else :
# # # #             print("error wrote operator")
# # # #
# # # # a =(input("Vvedite + ili - :"))
# # # #
# # # # counter=Counter(a)
# # # # counter.increment()
# # # # counter.increment()
# # # # counter.increment()
# # # # print(counter.getinfo())
# # # #
# # # # class Rectangle:
# # # #     def __init__(self, width, height):
# # # #         self.width = width
# # # #         self.height = height
# # # #     def getarea(self):
# # # #         return f"Rectangle area:{self.width * self.height}"
# # # #     def getperimetr(self):
# # # #
# # # #         return f"Rectange perimeter:{2*(self.width + self.height)}"
# # # #
# # # # a=int(input("width: "))
# # # # b=int(input("height: "))
# # # #
# # # # rectangle=Rectangle(a,b)
# # # # print(rectangle.getarea())
# # # # print(rectangle.getperimetr())
# # #
# # # # class Student:
# # # #     def __init__(self,name,grade):
# # # #         self.name=name
# # # #         self.grade=grade
# # # #
# # # #     def getinfo(self):
# # # #         return f"Name: {self.name} \nGrade: {self.grade}"
# # # #
# # # # student=Student("Davron","11")
# # # # print(student.getinfo())
# # #
# # # # class BankAccount:
# # # #     def __init__(self, account_number, balance):
# # # #         self.account_number = account_number
# # # #         self.balance = balance
# # # #
# # # #     def deposit(self, amount):
# # # #         self.balance += amount
# # # #         return self.balance
# # # #
# # # #     def witdraw(self, amount):
# # # #         if self.balance - amount > 0:
# # # #             self.balance -= amount
# # # #             return self.balance
# # # #         else:
# # # #             return print("Insufficient founds")
# # # #
# # # #     def getbalance(self):
# # # #         return self.balance
# # # #
# # # #
# # # # user = BankAccount(824356, 120000)
# # # # user.witdraw(130000)
# # # # print(user.getbalance())
# # # #
# # #
# # # # class Point:
# # # #     color =  "red"
# # # #     cicrle = 2
# # # #
# # # #     def set_cords():
# # # #         print("metod obyavlyaetsa")
# # # #
# # # # Point.set_cords()
# # # # s={1}
# # # # a= [{1:[2,3]} , {2:[3,4]}]
# # # # b=a[0].keys()
# # # #
# # # # if b==s:
# # # #     print("togri")
# # # # print(b)
# # #
# # # #
# # # # def even(quan: int = 10):
# # # #     even=[]
# # # #
# # # #     for x in range (abs(quan)):
# # # #         if not x%2:
# # # #             if quan<0:
# # # #                 even.append(-x)
# # # #             else :
# # # #                 even.append(x)
# # # #     return even
# # # #
# # # # def test():
# # # #     assert even(10) == [0,2,4,6,8]
# # # #     assert even(-4) == [0,-2]
# # # #
# # # #
# # # # test()
# # #
# # # class Student:
# # #
# # #     def __init__(self,name,age,region):
# # #         self.name=name
# # #         self.age=age
# # #         self.region = region
# # #
# # #
# # #     def ulug(self):
# # #
# # #     @property
# # #
# # #     def name_(self):
# # #         return self.region
# # #
# # #     @name_.setter
# # #
# # #     def name_(self, reg):
# # #         self.region = reg
# # #         return self.region
# # #
# # #
# # # n Student("Abbos",23,"Andijan")
# # # ulame1=ugbek=Student()
# # # print(name1.__dict__)
# # # name1.name_="Tashkent"
# # # print(name1.name_)
# # #
# # # class Jinnili:
# # #     pass
# #
# # class Human:
# #     name = "Abbos"
# #     age = 23
# #     profes = "programmer "
# #
# #     def __init__(self,ism,yosh,kasb):
# #         self.name = ism
# #         self.age = yosh
# #         self.profes = kasb
# #
# #
# # class Human1:
# #
# #     def __init__(self,name,age,profes):
# #         self.name = name
# #         self.age = age
# #         self.prafes = profes
# # long_string = "Это очень длинная строка, которая стала такой длинной, что ее трудно прочитать. \
# # Мы можем разбить ее на несколько линий, чтобы сделать ее более читабельной."
# #
# # print(long_string)
#
# class Person:
#     def __init__(self,first_name,last_name,age,passport,addres,birth_date,where_born):
#         self.first_name=first_name
#         self.last_name=last_name
#         self.age=age
#         self.passport=passport
#         self.addres=addres
#         self.birth_date=birth_date
#         self.where_born=where_born
#         self.conditio = "Alive"
#
#     def get_firtstname(self):
#         return self.first_name
#
#     def get_lastname(self):
#         return self.last_name
#
#     def get_fullname(self):
#         return self.last_name +self.first_name
#
#     def set_firstname(self,firsname):
#         self.first_name=firsname
#         return self.first_name
#     def set_lastname(self,lastname):
#         self.last_name=lastname
#         return self.last_name
#
#     def set_fullname(self,lastname,firstname):
#         self.last_name=lastname
#         self.first_name = firstname
#         return f"{self.last_name} {self.first_name}"
#
#     @property
#     def getset(self):
#         return self.age
#
#     @getset.setter
#     def getset(self,age):
#         self.age=age
#         return self.age
#
#     @staticmethod
#     def toupper(text):
#         return text.upper(,,,,,,,,,,,,,,,,
#\\
#     @classmethod
#     def condition(cls,conditio):
#
