class InsufficientBalanceError(Exception):
    """"Exception raised for insufficient account balance"""
    pass

class BankSystem:
    def __init__(self):
        self.accounts = []
        self.bank_service = BankService(self.accounts)

    def start_bank(self):
        print('Welcome to Banking Service!!')

        try:
            while True:
                user_input = int(input(
                    "\n1. Create Account\n"
                    "2. Deposit\n"
                    "3. Withdraw\n"
                    "4. View Accounts\n"
                    "5. Update Account\n"
                    "6. Delete Account\n"
                    "7. Exit\n"
                    "Enter choice: "
                ))

                if user_input == 1:
                    acc = self.bank_service.createAccount()
                    self.accounts.append(acc)
                    print("Account created successfully!")

                elif user_input == 2:
                    self.bank_service.deposit()

                elif user_input == 3:
                    self.bank_service.withdraw()

                elif user_input == 4:
                    self.bank_service.listAccounts()
                
                elif user_input == 5:
                    self.bank_service.updateAccount()

                elif user_input == 6:
                    self.bank_service.deleteAccount()

                elif user_input == 7:
                    print("Thank you for using Banking Service!")
                    break

                else:
                    print("Enter a valid option!")
        except ValueError:
            print("Enter integer value")


class BankAccount:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalanceError
        else:
            self.balance -= amount


class BankService:
    def __init__(self, accounts):
        self.accounts = accounts

    def createAccount(self):
        name = input("Enter account name: ").title()
        address = input("Enter address: ")

        while True:
            phone = input("Enter phone number: ")
            if len(phone) == 10 and phone.startswith(("97", "98")):
                break
            for acc in self.accounts:
                if phone == acc.phone:
                    print("Account already exists")

            print("Invalid phone number!")

        while True:
            email = input("Enter email: ")
            if email.endswith("@gmail.com"):
                break
            for email in self.accounts:
                if email == acc.email:
                    print("Account already exists")
            print("Invalid email!")

        return BankAccount(name, address, phone, email)

    def findAccount(self, name):
        for acc in self.accounts:
            if acc.name == name:
                return acc
        return None

    def deposit(self):
        name = input("Enter account name: ").title()
        acc = self.findAccount(name)
        if acc:
            amount = int(input("Enter amount to deposit: "))
            acc.deposit(amount)
            print("Deposit successful!")
        else:
            print("Account not found!")

    def withdraw(self):
        name = input("Enter account name: ").title()
        acc = self.findAccount(name)
        if acc:
            amount = int(input("Enter amount to withdraw: "))
            acc.withdraw(amount)
        else:
            print("Account not found!")

    def listAccounts(self):
        if not self.accounts:
            print("No accounts available.")
            return

        for acc in self.accounts:
            print(f"\nName: {acc.name}")
            print(f"Balance: {acc.balance}")
            print(f"Email: {acc.email}")

    def updateAccount(self):
        upname = input("Enter account name: ").title()
        acc = self.findAccount(upname)
        if not acc:
            print("account not found")
            return
        newname = input(f"\nOld Name: {acc.name} \nEnter New Name: ")
        if newname.strip():
            acc.name = newname.title()

        while True:
            newphone = input(f"Old phone: {acc.phone} \n Enter New Phone: ")
            if len(newphone) == 10 and newphone.startswith(("97", "98")):
                acc.phone = newphone
                break
            print("Invalid phone number!")

        while True:
            newmail = input(f"Old Email: {acc.email} \n Enter new Email: ")
            if newmail.endswith("@gmail.com"):
                acc.email = newmail
                break
            print("Invalid email!")
        
        print("Account updated Successfully")

    def deleteAccount(self):
        upname = input("Enter account name: ").title()
        acc = self.findAccount(upname)
        if acc:
            self.accounts.remove(acc)
            print("Account deleted Successfully!")
            
        else:
            print("Account not found")


def main():
    bank = BankSystem()
    bank.start_bank()


if __name__ == "__main__":
    main()
