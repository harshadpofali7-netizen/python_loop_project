#Mini project 6 : Electricity usage analyze
num_days = int(input("Enter the number of days to analyze:"))
total_units = 0
high_usage_days_count = 0
max_daily_uasge = 0.0

for day in range(1, num_days +1):
    units = float(input(f"Enter units consumed for days {day}: "))
    total_units += units
    if units > 10:
        high_usage_days_count += 1
    if units > max_daily_uasge:
        max_daily_uasge = units
average_uasge = total_units / num_days if num_days > 0 else 0

usage_status = "High Usage" if total_units > 300 else "Normal Usage"
print("\n" + "="*30)
print("    ELECTRICITY ANALYSIS    ")
print("\n" + "="*30)
print(f"Total units:    {total_units:}")
print(f"Average usage:   {average_uasge:}")
print(f"High-usage days:    {high_usage_days_count} (over 10 units)")
print(f"Maximum daily usage: {max_daily_uasge:}")
print("="*30)
