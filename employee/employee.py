
# class College:
#     name = "jkc"
#     print("inside of the class: ",name)
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id 
#         print("inside of the constructer: ",self.name)
#         print("inside of the constructer: ",self.id)
#     def display(self):
#         self.city = "guntur"
#         College.area = "AP"
#         address = "jkc nagar"
#         print("inside of the instance methode:",self.city)
#         print("inside of class method: ",College.area)
#         print("inside of local variable: ",address)
#     @classmethod
#     def m1(cls):
#         College.roll = "10"
#         cls.roll = "10"
#         print("inside of class methode: ",College.roll)
#         print("inside of class methode: ",cls.roll)
#     @staticmethod
#     def m2():
#         College.pincode = "522019"
#         College.group = "mecs"
#         print("inside of static method: ",College.pincode)
#         print("inside of static method: ",College.group)
            
        
# obj = College("srikanth","481") 
# obj.display()
# obj.m1()
# obj.m2()
# obj.College = "NCC"
# print("outside of the classs:",obj.College) #instance variable
# College.country = "INDIA"
# print("outside static method: ",College.country)


class Calculater:
    @staticmethod
    def sum(a,b):
        sum_1 = int(input("Enter sum_1: "))
        print(a + b)
    def product(a,b):
        product_1 = int(input("Enter product_1: "))
        print(a * b)
    def division(a,b):
        division_1 = int(input("Enter division_1: "))
        print(a//b)
    def modules(a,b):
        modules_1 = int(input("Enter division_1: "))
        print(a%b)
Calculater.sum(2,3)
Calculater.product(2,3)
Calculater.division(2,3)
Calculater.modules(2,3)
        

    