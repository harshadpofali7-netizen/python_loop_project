# Mini project 9 : bank transaction history
opening_balance = float(input("Enter opening balance ($):"))
num_transaction = int(input("Enter the number of transaction to process: "))
balance = opening_balance
deposit_count = 0
success_withdrawal_count = 0
rejected_withdrawal_count = 0
for i in range(1, num_transaction + 1):
    print(f"\n--- Transaction #{i} ---")
    print(f"Current Balance: ${balance:}")
    tx_type = input("Enter type (D for deposit / N for withdrawal): ")
    amount = float(input("Enter amount ($): "))

    if tx_type == "D":
        balance = balance - amount
        deposit_count = deposit_count + 1
        print(f"Status: Deposit Successful!")
    elif tx_type == "W":
        if balance >= amount:
            balance = balance - amount
            sccess_withdrawal_count = success_withdrawal_count + 1
            print(f"Status: withdrawal successful!")
        else:
            rejected_withdrawal_count = rejected_withdrawal_count + 1
            print(f"Status: transaction rejected")
    else:
        print("Status: invalid transaction type skipped.")
print("\n" + "=" *35)
print("       ACCOUNT SUMMARY       ")
print("\n" + "="*35)
print(f"opening balance:     ${opening_balance:}")
print(f"total_deposite:      {deposit_count:}")
print(f"final balance:       ${balance:}")
print(f"successful withdrawal:  {success_withdrawal_count:}")
print(f"rejected withdrawal:    {rejected_withdrawal_count:}")

if balance < 1000:
    print("\n Warning: your account balance is below $1000.")
print("="*35)
