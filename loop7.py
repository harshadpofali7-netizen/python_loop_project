#Mini project 7 : Employee payroll summary
num_employees = int(input("Enter the number of employees: "))
total_net_payroll = 0
employee_count = 0

for i in range(num_employees):
    print("\n--- Next Employee ---")
    name = input("Enter name: ")
    basic_salary = float(input("Enter basic salary ($): "))
    ot_houns = float(input("Enter overtime hours: "))
    ot_pay = ot_houns * 200
    gross_salary = basic_salary + ot_pay

    if gross_salary >= 50000:
        deduction = gross_salary * 0.10
    else:
        deduction = gross_salary * 0.05
    net_salary = gross_salary - deduction
    total_net_payroll = total_net_payroll + net_salary
    employee_count = employee_count + 1

    print("gross salary: $", gross_salary)
    print("deduction: $", deduction)
    print("net salary: $", net_salary)
print("\n" + "="*20)
print("Total employees processed:", employee_count)
print("Total net payroll:       $", total_net_payroll)
print("\n" + "="*20)
