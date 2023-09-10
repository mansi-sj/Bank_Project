# Bank class which serves blueprint for creating bank acc. It includes methods for operations like logging in,logging out,depositing money,withdrawing money,viewing balance,tranfering money, and displaying user details

class Bank: #class created of name Bank
    __usercount = 0 #Class var that keeps track of number of users It is private

    def __init__(self, name, gender, salary, pin): #constructore method when new instance of class is created
        # Here name,gender,salary,pin is initialize  and they are instance var which store infomation of each user
        self.name = name
        self.gender = gender
        self.salary = salary
        self.pin = pin
        Bank.__usercount += 1 #increments usercount each time when new user is created
        self.account_no = f"accno000{Bank.__usercount}" #this is generated based on user count
        #initialize user ststus and balance
        self.logged_in = False #it is initialized to False becoz user is not consider log in by deafult
        self.__balance = 0 #Make balance an instance variable and initilize balance 
 

    def login(self): #This defines a method named login which allows a user to log in.

        #Prompt user for pin amd verify 
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            self.logged_in = True
            print(f"Welcome, {self.name}!")
        else:
            print("Invalid Pin. Please try again.")

    def logout(self):#Logout for user
        self.logged_in = False #This sets self.logged_in to False, indicating that the user has logged out.


    def is_logged_in(self): #check if user is login or not
        return self.logged_in #It returns the value of self.logged_in, indicating whether the user is currently logged in.


    def deposit(self, amount): #This method allows the user to make a deposit.
        if self.is_logged_in(): #It first checks if the user is logged in.
        #deposite money if login
            self.__balance += amount  # Use private instance variable
            print("Deposit of", amount, "successful.")
            print(f"Amount of Rs{amount} has been deposited to {self.name}'s account.")
            self.view_balance()
            #If the user is logged in, it adds the amount to self.__balance, prints a success message, and displays the updated balance.
        else:
            print("Please login to perform this operation.")
            #If the user is not logged in, it prompts the user to log in.


    def withdraw(self, amount): #This method allows the user to make a withdrawal.
        if self.is_logged_in(): #It first checks if the user is logged in.
            if amount > self.__balance: #checks if sufficient balance for withdrawal
                print("Insufficient balance.")
            elif 100 <= amount <= self.__balance: #If the withdrawal amount is between 100 and the balance, it subtracts the amount from self.__balance, prints a success message, and displays the updated balance.
                self.__balance -= amount
                print("Thank you for visiting. Withdrawal of", amount, "successful.")
                self.view_balance() #If the withdrawal amount is less than 100, it prints an error message.
            else:
                print("You cannot withdraw less than 100.")
                self.view_balance()
        else: #If the user is not logged in, it prompts the user to log in.
            print("Please login to perform this operation.")

    def view_balance(self): #This method allows the user to view their balance.
        if self.is_logged_in():
            self.show_details() #display user details and balance if log in
            print("Balance:", self.__balance)
        else:
            print("Please login to perform this operation.")

    def transfer(self, amt, user): #This method allows the user to view their balance.
        if self.is_logged_in():#It checks if the user is logged in and if the transfer amount is valid.
            if amt > self.__balance: #checks if sufficient balance for transfer
                print("Insufficient balance.")
            elif 1 <= amt <= self.__balance:  #transfer money if condition met
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

    def show_details(self): #display user details
        print(f"Name: {self.name}, Gender: {self.gender}, Salary: {self.salary}, Account No: {self.account_no}")


def show_menu(): #display menu options #show_menu is funct displays available banking operations..
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Transfer")
    print("5. Logout")
    print("6. Exit")



#this is main loop where user interacts with bank. It presents options to create an acc,login or exit.
#Code is responsible for managing interactions with user.it presents options to create new acc,log in or exit program
users = {} #users = {} - This is a dictionary that will store user objects. The keys will be user names.
while True: #loop is the main loop of the program. It continuously prompts the user for input until they choose to exit.
    print("1. Create Account\n2. Login\n3. Exit")
    c = input("Enter your Selection : ")

    if c == "1":
        name = input("Enter your Name : ")
        gender = input("Enter your Gender : ")
        salary = float(input("Enter your Salary : "))
        pin = input("Set your Password : ")
        users[name] = Bank(name, gender, salary, pin)

    elif c == "2":
        #this is main loop where user interacts with bank. It presents options to create an acc,login or exit.
        # login to existing one
        name = input("Enter your Name : ")
        #Here, users.get(name, 0) attempts to retrieve the value associated with the key name from the users dictionary.
#If the name exists in the dictionary, obj will be set to the corresponding value (which is an instance of the Bank class representing the user).
#If the name is not found, obj will be set to 0 (which serves as an indicator that no match was found).

        obj = users.get(name, 0) #This condition checks whether obj is equal to 0. If it is, it means no matching user was found in the users dictionary.


        if obj == 0: #If no matching user was found, this message is printed to inform the user.

            print("No Match Found")
            continue #The continue statement means that the program will jump back to the start of the loop. In this context, if no match is found, the program will go back to the point where it prompts the user to select an option (create an account, log in, or exit).

        else: #If a matching user was found, this block of code will execute.
            obj = users[name] #Here, obj is reassigned to the user object associated with the name in the users dictionary. This step ensures that obj holds the correct user object for subsequent operations.


        obj.login() #Finally, the login() method of the user object is called. This prompts the user to enter their PIN and attempts to log them in.


        while obj.is_logged_in():   # While logged in, display the menu and perform operations

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
#If the user chooses to exit, the program breaks out of the loop and terminates.
#This block handles the options when the user chooses to log in. It allows the user
