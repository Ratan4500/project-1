Name = str(input("Enter the name : "))
monthly_income = int(input("Enter the income amount : "))
rent_amount = int(input('Enter the rent amount : '))
trevel_expenses = int(input('Enter the trevel amount : '))
food_expenses = int(input('Enter the food amount : '))
entertainment = int(input('Enter the entertainment amount : '))
other_expenses = int(input('Enter the others amount : '))

total_expenses = rent_amount+trevel_expenses+food_expenses+entertainment+other_expenses
remain_amount = monthly_income - total_expenses
saving_percentage = (remain_amount/monthly_income)*100

print("================MONTHLY EXPENSES REPORT=======================")

print("Name : ",Name)
print("Monthly_income : ",monthly_income)
print("Total expenses : ",total_expenses)
print("Remaining amount : ",remain_amount)
print("Saving percentage : ", saving_percentage,"%")
