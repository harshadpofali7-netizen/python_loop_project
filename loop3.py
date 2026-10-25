#Mini project 3 : ATM pin verification
CORRECT_PIN = "1234"
attempt_used = 0
max_attempts = 3
access_granted = False
while attempt_used < max_attempts:
    user_entry = input(f"Enter your 4-digit ATM PIN (attempt {attempt_used + 1}/{max_attempts}): ")
    attempt_used += 1
    if user_entry == CORRECT_PIN:
        print("\nAccess granted")
        access_granted = True
        break
    else:
        print("Incorect PIN.")
        remaining = max_attempts - attempt_used
        if remaining > 0:
            print(f"You have {remaining} attempt left.\n")

print("\n---TRANSACTION SUMMARY---")
print(f"Access status: {'approved' if access_granted else 'Denied'}")
print(f"Attempt used: {attempt_used}")
if not access_granted and attempt_used == max_attempts:
    print("Lock massage: Card temprarily locked")
print("--------------------------")
