import time

print("Please insert Your CARD")
time.sleep(5)

password = "0000"
pin = input("Enter your ATM pin: ")
balance = 10000
if pin == password:
    while True:
        print(""" 
			1 == balance
			2 == withdraw balance
			3 == deposit balance
            4 == transfer balance 
			5 == exit
			""")
        try:
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue

        if option == 1:
            print(f"Your current balance is {balance}")

        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            if withdraw_amount > balance:
                print("Insufficient balance")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {balance}")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")

        elif option == 4:
             account_name = str(input("please enter name of the account: "))
             transfer_ammount =int(input("please enter trasfer amount: "))
             if transfer_ammount > balance:
                print("Insufficient balance")
             else:   
                balance -= transfer_ammount
                print(f"{transfer_ammount} is transfered to {account_name}")
                print(f"your updated balance is {balance} ")
                
        elif option == 5:
            break

else:
    print("Wrong pin. Please try again.")
