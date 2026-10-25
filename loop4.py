#Mini project 4: Shopping cart total
num_product = int(input("Enter the number of product to check out: "))
grand_subtotal = 0.0
for i in range(1, num_product + 1):
    print(f"\n--- Item{i} ---")
    while True:
        price = float(input("Enter unit price (in $): "))
        quantity = int(input("Enter quantity: "))
        if price >= 0 and quantity >= 0:
            break
        print("Invalid enter! Price and quantity cannot be negative.")
    item_subtotal = price * quantity
    grand_subtotal += item_subtotal
if grand_subtotal >= 3000:
    discount = grand_subtotal * 0.10
else:
    discount = 0.0
discount_amount = grand_subtotal - discount
if discount_amount < 1500:
    delivery_charge = 100.0
else:
    delivery_charge = 0.0
final_payable = discount_amount + delivery_charge
print("\n==========================")
print("     SHOPPING RECEIPT       ")
print("============================")
print(f"Subtotal       :${grand_subtotal}")
print(f"Discount (10%) :${discount}")
print(f"Delivery charge:${delivery_charge}")
print("-----------------------------------")
print(f"Final payable amount:${final_payable}")
print(f"=======================================")
