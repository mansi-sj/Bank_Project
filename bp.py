'''class Bank: #class created of name Bank
    __usercount = 0 #Class var that keeps track of number of users It is private 


def __init__(self, name, gender, salary, pin): #constructore method when new instance of class is created
        # Here name,gender,salary,pin is initialize  and they are instance var which store infomation of each user
        self.name = name
        self.gender = gender
        self.salary = salary
        self.pin = pin
        Bank.__usercount += 1 #increments usercount each time when new user is created
        self.account_no = f"accno000{Bank.__usercount}" #this is generated based on user count
        self.logged_in = False #it is initialized to False becoz user is not consider log in by deafult
        self.balance = 0  # Make balance an instance variable and initilize balance 

    def login(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            self.logged_in = True
            print(f"Welcome, {self.name}!")
        else:
            print("Invalid Pin Please try again.")

    def logout(self):
        self.logged_in = False

    def is_logged_in(self):
        return self.logged_in

    def deposit(self, amount):
        if self.is_logged_in():
            self.balance += amount  # Use instance variable
            print("Deposit of", amount, "successful.")
            print(f"Amount of Rs{amount} has been deposited to {self.name}'s account.")
            self.view_balance()
        else:
            print("Please login to perform this operation.")

    def withdraw(self, amount):
        if self.is_logged_in():
            if amount > self.balance:
                print("Insufficient balance.")
            elif 100 <= amount <= self.balance:
                self.balance -= amount
                print("Thank you for visiting. Withdrawal of", amount, "successful.")
                self.view_balance()
            else:
                print("You cannot withdraw less than 100.")
                self.view_balance()
        else:
            print("Please login to perform this operation.")

    def view_balance(self):
        if self.is_logged_in():
            self.show_details()
            print("Balance:", self.balance)
        else:
            print("Please login to perform this operation.")

    def transfer(self, amt, user):
        if self.is_logged_in():
            if amt > self.balance:
                print("Insufficient balance.")
            elif 1 <= amt <= self.balance:
                self.balance -= amt
                if user:
                    user.deposit(amt)
                    print("Rs", amt, "transferred successfully.")
                    print(f"You transferred Rs{amt} to {user.name}.")
                    self.view_balance()
                else:
                    print("User not found.")
            else:
                print("You cannot transfer less than 1.")
                self.view_balance()
        else:
            print("Please login to perform this operation.")

    def show_details(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Salary: {self.salary}, Account No: {self.account_no}")


def show_menu():
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Transfer")
    print("5. Logout")
    print("6. Exit")


users = {}

while True:
    print("1. Create Account\n2. Login\n3. Exit")
    c = input("Enter your Selection : ")

    if c == "1":
        name = input("Enter your Name : ")
        gender = input("Enter your Gender : ")
        salary = float(input("Enter your Salary : "))
        pin = input("Set your Password : ")
        users[name] = Bank(name, gender, salary, pin)

    elif c == "2":
        name = input("Enter your Name : ")
        obj = users.get(name, 0)

        if obj == 0:
            print("No Match Found")
            continue
        else:
            obj = users[name]

        obj.login()

        while obj.is_logged_in():
            show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter the amount to deposit: "))
                obj.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter the amount to withdraw: "))
                obj.withdraw(amount)
            elif choice == '3':
                obj.view_balance()
            elif choice == '4':
                amount = float(input("Enter the amount to transfer: "))
                other_user = input("Enter the name of the user to transfer to: ")
                obj.transfer(amount, users.get(other_user))
            elif choice == '5':
                obj.logout()
                print("Logged out successfully.")
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
    elif c == "3":
        break

# Example users
user1 = Bank("Mansi", "Female", 5000, '1234')
user2 = Bank("Kasturi", "female", 8000, '5678')'''
class Bank:
    __usercount = 0

    def __init__(self, name, gender, salary, pin):
        self.name = name
        self.gender = gender
        self.salary = salary
        self.pin = pin
        Bank.__usercount += 1
        self.account_no = f"accno000{Bank.__usercount}"
        self.logged_in = False
        self.__balance = 0  # Make balance a private instance variable

    def login(self):
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            self.logged_in = True
            print(f"Welcome, {self.name}!")
        else:
            print("Invalid Pin. Please try again.")

    def logout(self):
        self.logged_in = False

    def is_logged_in(self):
        return self.logged_in

    def deposit(self, amount):
        if self.is_logged_in():
            self.__balance += amount  # Use private instance variable
            print("Deposit of", amount, "successful.")
            print(f"Amount of Rs{amount} has been deposited to {self.name}'s account.")
            self.view_balance()
        else:
            print("Please login to perform this operation.")

    def withdraw(self, amount):
        if self.is_logged_in():
            if amount > self.__balance:
                print("Insufficient balance.")
            elif 100 <= amount <= self.__balance:
                self.__balance -= amount
                print("Thank you for visiting. Withdrawal of", amount, "successful.")
                self.view_balance()
            else:
                print("You cannot withdraw less than 100.")
                self.view_balance()
        else:
            print("Please login to perform this operation.")

    def view_balance(self):
        if self.is_logged_in():
            self.show_details()
            print("Balance:", self.__balance)
        else:
            print("Please login to perform this operation.")

    def transfer(self, amt, user):
        if self.is_logged_in():
            if amt > self.__balance:
                print("Insufficient balance.")
            elif 1 <= amt <= self.__balance:
                self.__balance -= amt
                if user:
                    user.deposit(amt)
                    print("Rs", amt, "transferred successfully.")
                    print(f"You transferred Rs{amt} to {user.name}.")
                    self.view_balance()
                else:
                    print("User not found.")
            else:
                print("You cannot transfer less than 1.")
                self.view_balance()
        else:
            print("Please login to perform this operation.")

    def show_details(self):
        print(f"Name: {self.name}, Gender: {self.gender}, Salary: {self.salary}, Account No: {self.account_no}")


def show_menu():
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Transfer")
    print("5. Logout")
    print("6. Exit")


users = {}

while True:
    print("1. Create Account\n2. Login\n3. Exit")
    c = input("Enter your Selection : ")

    if c == "1":
        name = input("Enter your Name : ")
        gender = input("Enter your Gender : ")
        salary = float(input("Enter your Salary : "))
        pin = input("Set your Password : ")
        users[name] = Bank(name, gender, salary, pin)

    elif c == "2":
        name = input("Enter your Name : ")
        obj = users.get(name, 0)

        if obj == 0:
            print("No Match Found")
            continue
        else:
            obj = users[name]

        obj.login()

        while obj.is_logged_in():
            show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter the amount to deposit: "))
                obj.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter the amount to withdraw: "))
                obj.withdraw(amount)
            elif choice == '3':
                obj.view_balance()
            elif choice == '4':
                amount = float(input("Enter the amount to transfer: "))
                other_user = input("Enter the name of the user to transfer to: ")
                obj.transfer(amount, users.get(other_user))
            elif choice == '5':
                obj.logout()
                print("Logged out successfully.")
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")
    elif c == "3":
        break

