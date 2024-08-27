print('Welcome to Tip Calculator')
total = float(input("What was the total bill: "))
tip = int(input("How much would you like to tip? "))
split = int(input('How many people to split the bill? '))
per_head = (total + (total * (tip/100)))  / split
print("Each person has to pay: ",round(per_head,2))