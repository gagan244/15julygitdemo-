name = input("Plz Enter Your Name : ")
print("Hello",name)
message = """
Please select any of them option,
Type 1 >>>> CHECK BALANCE.
Type 2 >>>> DEPOSIT.
Type 3 >>>> WITHDRAWL.
"""
print(message)
task = int(input('Plz choose any option: '))
available_amount = 50000

if task >=1 and task <= 3: # 1to 3
  print('welcome to ATM')

  if task == 1:
    print('Thanks for visiting us, your available balance is',available_amount)
  elif task == 2:
    #deposite amount
    deposite_amount = int(input('Plz enter your deposite amount: '))
    if deposite_amount >= 500:
      #deposite_task
      available_amount = available_amount + deposite_amount#availabe_amount += deposite_amount
      print('You have successfully deposite your amount: ', available_amount)
      print('Thanks for visiting us')

    else:
      print('Plz deposite more than 500')
  elif task == 3:
        withdraw_amount = int(input('Plz enter your withdrawal amount: '))
        if withdraw_amount <= available_amount:
            # Withdraw task
            available_amount -= withdraw_amount
            print('You have successfully withdrawn your amount. New balance:', available_amount)
            print('Thanks for visiting us')
        else:
            print('Insufficient balance')
else:
  print('invalid option')