
class BankAccount:
    def __init__(self, name:str ,balance: int , address:str, marital_status:str ,phone_no:int,email:str  ):
        self.name= name
        self.balance= balance
        self.address= address
        self.marital_status= marital_status    
        self.phone_no= phone_no
        self.email= email
    
    def Check_Balance(self):
        return f"Your Balance is {self.balance} "
    
    def Deposit(self):
        Amount=int(input("Enter the amount to be Deposited:"))
        if Amount >0:
            self.balance += Amount
        else:
            raise ValueError("The Amount Deposited cannot be Negative. Put Correct Value.")
    
    def Withdraw(self):
        Amount=int(("Enter the amount to be Withdrawed:"))
        if(Amount>self.balance):
            raise ValueError("Withdrawed Amount cannot be Greater than Your Current Balance")
        if(Amount<0):
            raise ValueError("INVALID AMOUNT!")   
        if(Amount<=self.balance):
            self.balance-=Amount   

class SavingAccount(BankAccount):

    ...

class CurrentAccount(BankAccount):
    pass

class BankService:
    def CreateAccount(self):
        while True:
            account_name = input('Enter your account name: ')
            account_name.title()
            address = input('Enter address: ')
            try:
                ph_no = input('Enter phone number: ')
                if len(ph_no) == 10 and ph_no.startswith('97' and '98'):
                    print("Phone number is valid.")
                    break
                else:
                    print('Enter valid number!(10 numbers and must start with 97 and 98)')
            except:
                print("try again")

            try:
                email = input("Enter email: ")
                # regex
                if '@gmail.com' in email:
                    print('Email is validated')
                    break
                else: 
                    print('Enter valid email(must have gmail.com)')
                
            except:
                print('try again')

        return {
                'Account Name': account_name,'Address': address, "Phone Number": ph_no, 
                "Email": email
                }

    def findAccount():
        pass

    def listAccount():
        pass

def main():
    # Your main program logic goes here
    print("Hello, world!")
    bs = BankService()
    bs.Create_Account()

# The following checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()