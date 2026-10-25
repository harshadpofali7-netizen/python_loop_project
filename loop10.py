# Mini project 10 : Multiplication table and number analyzer
table_num = int(input("Enter a positive integer for the multiplication table: "))
while True:
    start_num = int(input("Enter the start of the number range: "))
    end_num = int(input("Enter the end of the number range: "))

    if start_num <= end_num:
        break
    else:
        print("Validation error: start number cannot be greater than end number.")
print(f"\n--- Multiplication table for {table_num} ---")
for i in range(1, 11):
    product = table_num * i
    print(f"{table_num} x {i} = {product}")

even_count = 0
odd_count = 0
range_sum= 0
for num in range(start_num, end_num + 1):
    range_sum = range_sum + num
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print("\n" + "="*30)
print(f"     RANGE ANALYSIS     ")
print("="*30)
print(f"total sum of range: {range_sum}")
print(f"total even numbers: {even_count}")
print(f"total odd numbers: {odd_count}")
print("="*30)
