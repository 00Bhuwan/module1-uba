def makeAccount():
    while True:
        account_name = input('Enter your account name: ')
        account_name.title()
        account_number = 'generate accordingly'
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
            if '@gmail.com' in email:
                print('Email is validated')
                break
            else: 
                print('Enter valid email(must have gmail.com)')
            
        except:
            print('try again')

    return {
            'Account Name': account_name, 'Account Number': account_number,
            'Address': address, "Phone Number": ph_no, 
            "Email": email    
                }
    
accoumt_details = makeAccount()
print(accoumt_details)