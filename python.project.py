print("WELOCOME TO THE ATM")
#showing the user his/her name.
print("NAME: MR.JOHN")
#amount avaliable in user account
balance=10000
print("Savings in your account:",balance)
#Showing  info to user

print(""" choose your service 
			1-balance enquiry
			2-withdraw cash
			3-deposit cash
			4-exit
			""")   
 #taking an option from user
option = int(input("Please enter your choice: "))
        
 #for option 1        
if option == 1:
    print(f"Your current balance is {balance}")
    print("Thank you!\nVisit Again")
                            
#for option 2
elif option == 2:
    withdraw_amount = int(input("please enter withdraw_amount : "))
    if  withdraw_amount<=balance:
        balance = balance - withdraw_amount
        print(f"{withdraw_amount} is debited from your account")
        print(f"Your updated balance is {balance}")
        if balance<5000:
            print("Low Balance")
        else:
            print("Thank you!\nVisit Again")
    else:
        print("Insufficient Amount")

            
#for option 3
elif option == 3:
    deposit_amount = int(input("Please enter deposit_amount : "))
    balance = balance + deposit_amount
    print(f"{deposit_amount} is credited to your account")
    print(f"Your updated balance is {balance}")
    print("Thank you!\nVisit Again")
    
#for option 4
elif option==4:
    print("thank you!\nVisit Again")
    
#for low balance
else :
    print("Choose your correct service")

           


