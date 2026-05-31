class Atm():
    def __init__(self):         #constructor
        self.balance = 0
        self.pin = ""
        self.menu()

    def menu(self):
        while True:   # <-- LOOP THE MENU
            user_input = int(input("""
                                   Press 1 to set your pin
                                   Press 2 to deposit money
                                   Press 3 to withdraw money
                                   Press 4 to check balance
                                   Press 5 to exit
                                   Choose an option: """))
                                      
            if user_input == 1:
                self.create_pin()
            elif user_input == 2:
                self.deposit()
            elif user_input == 3:
                self.withdraw()
            elif user_input == 4:
                self.check_balance()
            elif user_input == 5:
                print("Bye!")
                break
            else:
                print("Invalid option")

    def create_pin(self):
        self.pin = int(input("Enter pin: "))
        print("Pin set successfully!")

    def deposit(self):
        temp = int(input("Enter Pin: "))
        if temp == self.pin:
            amt = int(input("Enter amount to deposit: "))
            self.balance += amt
            print("Deposit successful!")
        else:
            print("Invalid pin")

    def withdraw(self):
        temp = int(input("Enter Pin: "))
        if temp == self.pin:
            amt = int(input("Enter amount to withdraw: "))
            if amt <= self.balance:
                self.balance -= amt
                print(f"Withdrawal of {amt} is successful!")
            else:
                print("Insufficient balance")
        else:
            print("Invalid pin")

    def check_balance(self):
        temp = int(input("Enter Pin: "))
        if temp == self.pin:
            print("Current balance:", self.balance)
        else:
            print("Invalid pin")


sbi = Atm()
