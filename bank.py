import os
from fpdf import FPDF

class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.statement = []

    def deposit(self, amount):
        self.balance += amount
        self.statement.append(f"Deposited {amount}")
        return f"Deposited {amount}. Current balance is {self.balance}"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.statement.append(f"Withdrew {amount}")
            return f"Withdrew {amount}. Current balance is {self.balance}"
        else:
            return "Insufficient balance"

    def download_statement(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, f"Account Statement for {self.account_number}", ln=True)
        pdf.cell(200, 10, f"Current Balance: RS.{self.balance}", ln=True)
        pdf_bytes = pdf.output(f"{self.account_number}_statement.pdf")

# Sample data for testing
accounts = {
    '123456': BankAccount('123456', '1234', 1000),
    '654321': BankAccount('654321', '4321', 500)
}

def create_account():
    account_number = input("Enter account number: ")
    pin = input("Set a 4-digit PIN: ")
    accounts[account_number] = BankAccount(account_number, pin)
    print("Account created successfully")

def login():
    account_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    if account_number in accounts and accounts[account_number].pin == pin:
        return accounts[account_number]
    else:
        return None

def main():
    while True:
        print("\n1. Create Account\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            account = login()
            if account:
                while True:
                    print("\n1. Deposit\n2. Withdraw\n3. Download Statement\n4. Logout")
                    option = input("Enter your choice: ")

                    if option == '1':
                        amount = float(input("Enter amount to deposit: "))
                        print(account.deposit(amount))
                    elif option == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        print(account.withdraw(amount))
                    elif option == '3':
                        if account:
                            account.download_statement()
                            print("Statement downloaded as PDF")
                        else:
                            print("Please create an account first")
                    elif option == '4':
                        break
                    else:
                        print("Invalid choice")
            else:
                print("Invalid account number or PIN")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()