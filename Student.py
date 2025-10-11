def messege():
    print("Welcome to the tech school!")
messege()

class Student:
    name=""
    age=11
    contact=""
    address=""
    club="badminton"
    school="The tech school"
    school_class="7L"

    def __init__(self):
        print("new student")
        
        self.name=input("enter your name ")
        self.contact=input("enter your contact number ")
        self.address=input("enter your address ")
        self.age=input("enter your age ")
    
    def display_data(self):
        print("Hello",self.name)
        print(f"the details for {self.name} are")
        print(f"age {self.age} ")
        print(f"contact {self.contact} ")
        print(f"address {self.address} ")
        print(f"club {self.club} ")
        print(f"school {self.school} ")
        print(f"school_class {self.school_class} ")

# Creating object of student class
student1 = Student()

# Displaying details
student1.display_data()




















