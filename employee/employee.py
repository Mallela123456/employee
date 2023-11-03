class Employee:
    M = "college"
    def __init__(self, name,id):
        self.name = name
        self.id  = id
        Employee.roll = "481"
        print("inside constructer:" ,Employee.roll)
    def method(self):
        print("name:",self.name)
        print("id:",self.id)
        Employee.address = "guntur"
        print("inside of instance method:",Employee.address)
    @classmethod
    def m3(cls):
        Employee.branch = "Mecs"
        cls.sub = "Electronics"
        print("inside the class methode: ", Employee.branch)
        print("inside the class methode: ", cls.branch)
    @staticmethod
    def m4():
        Employee.hallticket = "182342"
        print("inside the static methode: ", Employee.hallticket)
        
obj = Employee("srikanth","4")
obj.method()
obj.m3()
obj.m4()
Employee.groundname = "jkc"
print("outside of the methode:",Employee.groundname)



    