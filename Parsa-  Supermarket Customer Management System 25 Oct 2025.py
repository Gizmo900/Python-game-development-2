# Supermarket Customer Management System
#Homework: Displays a welcome message for the supermarket. 
# Uses a class (Customer) to manage customer data. 
# Prompts the user to enter customer details at the time of creating an object. 
# Allows the user to update details (e.g., address or membership type). 
# Displays a clean summary of customer information.
#
# --- Supermarket: Customer Management ---


def message():# Def means define a function.
    print("Welcome to our supermarket!")

class Customer:  # defines a class in Python called Customer.
    name = ""
    contact = ""
    address = ""
    items = ""
    supermarket = "Tesco"
    payment = ""

    def __init__(self): # Def means define a function.  __init__ means initialize(special function).
                        #Self refers to the object itself. It lets the object store its own data.
        print("New customer registration")
        self.name = input("Enter your name: ") # asks the user to type their name on the keyboard. Whatever the user types is saved inside the name variable.
        self.contact = input("Enter your contact number: ")
        self.address = input("Enter your address: ")
        self.items = input("Enter your items: ")
        self.payment = input("Enter your payment")

    def update_details(self):
        print("\n--- Update Details ---")
        choice = input("Do you want to update your address, contact, items or payment? (a/c/i/p none): ").lower() # waits for the user to type something (e.g., "A"),
                                                                                                                  #then .lower() converts that response to lowercase (so "A" → "a"),
                                                                                                                   #and finally assigns it to choice.
        if choice == "a":
            self.address = input("Enter new address: ")
        elif choice == "c":
            self.contact = input("Enter new contact number: ")
        elif choice == "i":
            self.items = input("Enter a new item: ")
        elif choice == "p":
            self.payment = input("Enter a new payment:")
        else:
            print("No updates made.")
   

    def display_data(self):
        print("\n--- Customer Information ---")
        print("Hello", self.name)
        print(f"The details for {self.name} are:")
        print(f"Items: {self.items}")
        print(f"Contact: {self.contact}")
        print(f"Address: {self.address}")
        print(f"Payment: {self.payment}")
        print(f"Supermarket: {self.supermarket}")
        
# Creating object of Student class
customer1 = Customer() # Creates a new object called customer1 (like a mini version of the class).

# Option to update details
customer1.update_details()

# Displaying details
customer1.display_data()

