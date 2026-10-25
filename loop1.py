# Mini project 1 : Daily expense tracker
num_days = int(input("Enter number of days to record: ")) 
total_expence = 0.0
highest_expence = 0.0
for day in range(1, num_days + 1):
    expence = float(input("Enter expence for day {day} (in $): "))
    total_expence += expence
    if expence > highest_expence:
        highest_expence = expence
if num_days > 0:
    average_expence = total_expence / num_days
else:
    average_expence = 0.0
if total_expence > 5000:
    budget_status = "Budget alert"
else:
    budget_status = "within budget"
print("\n---Expense summary---")
print(f"Total expence: ${total_expence}")
print(f"Average daily expence: ${average_expence}")
print(f"Highest daily expence: ${highest_expence}")
print(f"Budget status: {budget_status}")
