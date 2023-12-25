# import cv2
# import math
# print("hello world\n")
# print(5+8)
# print("Yunisha Regmi")
# print(math.gcd(3,6))
# a = 34
# b  = "yunisha"
# c = 45
# d = 3
# print(a%d)

# print(a+d)
# print(a-d)
# print(a*d)
# print(a/d)
# typeA =type(a)
# typeB =type(b)
# print(typeB)
# e = "31"
# e = float(e)
# # e = 3.14
# print(type(e))
# print(e+2)
# name = "Yunisha, Hima, Yojana"
# print(name[1:4])
# print(name.strip())
# print(len(name))
# var = name.upper()
# var = name.replace("is", "u")
# var = name.replace(", ", '\n')
# print(var)
# stri ="This is a "
# name = "Yunisha"
# name2 = "Yojana"
# stri2 = "this is not a"
# print(stri + name)
# temp = "This is a {1} ans she is a good girl named {0}".format(name, name2)
# temp = f"this is a {name2} and she is a good girl {name}"
# print(temp)

# lst = [61,2,3,4,6,41]
# lst.clear()
# var = type(lst)
# lst[2] = 45
# var = lst[2]
# lst.remove(6)
# del lst[3]

# del lst
# lst.pop(61)
# lst.insert(1,100)
# lst.append(100)
# var = lst
# var = len(lst)
# var = lst[1:4]
# print(var)


# a = ("Yunisha", "Yojana", "Hima")
# var = a
# a = list(a)
# var = type(a)
# a[0] = "unisha"
# print(var)

# s1 = {23,3,3,4,5,6,2,2,3,4,}
# s1.add(4444)
# s1.update([12,12,423,3423,87675,90,78])
# print(len(s1))
# s1.remove(3)
# s1.discard(66565)

# print(s1)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.intersection(y)

# print(z)

# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.union(y)

# print(z)


# YunishaDict = {
#     "Name": "Yunisha",
#     "Class" :"4thsem",
#     "Marks" :34.34,
#     "hours in school" : 6
# }

# YunishaDict["Marks"] =34
# print(YunishaDict["Marks"])
# YunishaDict.pop("Marks")
# print(YunishaDict)


# age = 34
# age = input("Enter your age\n")
# age = int(age)
# # print(type(age))
# if(age>18):
#     print("you can drive a car")

# elif(age==18):
#     # a= True
#     # b= False
#     print("you are an awesome teen")

# else:
#     print("you cannot drive")

# for i in range(0, 1000):
#     print(i+1)
# li =[1,432, "this"]
# for item in li:
#     print(item)
# i =0
# while(i<100):
#         # break
#     i=i + 1
#     if i == 78:
#          continue
#     print(i+1)
# def sum(a,b):
#     print("running sum")
#     c = a +b
#     return c
# d = sum(34 , 45)
# print(d)
# class employee:
#     def __init__(self, gname, gsalary):
#         self.name = gname
#         self.salary = gsalary 
# yunisha = employee("yunisha", 34)
# print(yunisha.name)
# print(yunisha.salary)

# class vehicle :
#     def __init__(self,milage,cost):
#         self.milage = milage
#         self.cost = cost
#     def show_details(self):
#         print("Iam vehicle")
#         print("Milage of vehicle is", self.milage)   
#         print("cost of vehicle is", self.cost)
# v1 = vehicle(500,500)
# v1.show_details()        

# class car(vehicle):
#     def showcar(self):
#         print("iam a car")
# c1= car(200,2000)
# c1.show_details()
# c1.showcar()
# class car(vehicle):
#     def  __init__(self, milage, cost,tyres,hp):
#         super().__init__(milage, cost)
#         self.tyres = tyres
#         self.hp = hp
#     def show_car_details(self):
#         print("iam a car")
#         print("number of tyres are",self.tyres)
#         print("value of horse power is",self.hp) 
# c1= car(20,12000,4,300)
# c1.show_details()
# c1.show_car_details()

# class parent1():
#    def  assign_string_one(self,str1):
#          self.str1 = str1
#          def show_string_one(self):
#             return self.str1  

# class parent2():
#       def assign_strng_two(self,str2):
#             self.str2 = str2
#             def show_string_two(self):
#                   return self.str2
            
# class Child(parent1,parent2):
#       def assign_string_three(self,str3):
#             self.str3 = str3
#             def show_string_three(self):
#                   return self.str3
# my_child = Child()
# my_child.assign_string_one("one")
# my_child.assign_strng_two("two")
# my_child.assign_string_three("three")
# my_child.show_string_one()
# my_child.show_string_two()
# my_child.show_string_three()
            
class parent():
    def assignname(self,name):
        self.name = name

    def showname(self):
        return self.name
class child(parent):
    def assignage(self,age):
        self.age = age
    def showage(self):
        return self.age

class grandchild(child):
    def assigngender(self,gender):
        self.gender = gender
    def showgender(self):
        return self.gender                             
gc = grandchild()
gc.assignname("yunisha")
gc.assignage(21)
gc.assigngender("female")  
gc.showname()