
# Q1 class Student and display name, age and registration no 
# class Student:
#     def __init__(self, name, age, reg_no):
#         self.name = name 
#         self.age = age
#         self.reg_no = reg_no
    
#     def display(self):
#         print("Student Name:", self.name)
#         print("Student age:", self.age)
#         print("Student Registration no:", self.reg_no)
        
# s1 = Student("Adina Zeeshan", 19, 1070)
# s2 = Student("Umar Farooq", 21, 1192)

# s1.display()
# s2.display() 





# Q2 make a class Vehicle and display brand, model, color, price 
class Vehicle():
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        
    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Color:", self.color)
        print("Price:", self.price)
        
v1 = Vehicle("Civic", 2024, "Black", 8950000)
v1.display()