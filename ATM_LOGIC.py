class Atm:
    def __init__(self):
        self.__balance = 0
        self.__pin = None
        self.menu()

    def menu(self):
        while True:
            try:
                user_input = int(input("""
Press 1 to set your pin
Press 2 to reset your pin
Press 3 to deposit money
Press 4 to withdraw money
Press 5 to check balance
Press 6 to exit
Choose an option: """))

                if user_input == 1:
                    self.create_pin()
                if user_input == 2:
                    self.reset_pin()
                elif user_input == 3:
                    self.deposit()
                elif user_input == 4:
                    self.withdraw()
                elif user_input == 5:
                    self.check_balance()
                elif user_input == 6:
                    print("Bye!")
                    break
                else:
                    print("Invalid option")

            except ValueError:
                print("Please enter a valid number.")

    def create_pin(self):
        pin = input("Enter PIN: ").strip()

        if not pin.isdigit():
            print("PIN should contain only digits.")
            return

        self.__pin = pin
        print("PIN set successfully!")

    def verify_pin(self):
        if self.__pin is None:
            print("No PIN set. Please create a PIN first.")
            return False

        temp = input("Enter PIN: ").strip()

        if temp == self.__pin:
            return True

        print("Invalid PIN")
        return False
    
    def reset_pin(self):
        if self.__pin is None:
            print("No PIN set. Please create a PIN first.")
            return False
        
        if not self.verify_pin():
            print("wroong pin")
            return
        
        new_pin = input("Enter NEW PIN: ").strip()
        confirm_pin = input("Confirm new PIN:   ").strip()

        if not new_pin.isdigit():
            print("PIN should contain only digits.")
            return
        
        if new_pin != confirm_pin:
            print("PINs don't match. Try again.")
            return

        self.__pin = new_pin
        print("PIN reset successfully!")        


    def deposit(self):
        if not self.verify_pin():
            return

        try:
            amt = int(input("Enter amount to deposit: "))

            if amt <= 0:
                print("Deposit amount must be positive.")
                return

            self.__balance += amt
            print("Deposit successful!")

        except ValueError:
            print("Please enter a valid amount.")

    def withdraw(self):
        if not self.verify_pin():
            return

        try:
            amt = int(input("Enter amount to withdraw: "))

            if amt <= 0:
                print("Withdrawal amount must be positive.")
                return

            if amt <= self.__balance:
                self.__balance -= amt
                print(f"Withdrawal of {amt} is successful!")
            else:
                print("Insufficient balance")

        except ValueError:
            print("Please enter a valid amount.")

    def check_balance(self):
        if not self.verify_pin():
            return

        print("Current balance:", self.__balance)


sbi = Atm()
