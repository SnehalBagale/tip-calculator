bill_amount = float(input("Enter the total bill amount (before tip): "))
if bill_amount <= 0:
    print("Error: Bill amount must be a positive number.")
    exit()

service_quality = input("Enter the quality of service (poor, fair, good, excellent): ").lower()

if service_quality == "poor":
    tip_percentage = 0.10
elif service_quality == "fair":
    tip_percentage = 0.15
elif service_quality == "good":
    tip_percentage = 0.18
elif service_quality == "excellent":
    tip_percentage = 0.20
else:
    print("Error: Invalid service quality.")
    exit()

num_people = int(input("Enter the number of people splitting the bill: "))
if num_people <= 0:
    print("Error: Number of people must be a positive integer.")
    exit()

tip_amount = bill_amount * tip_percentage
total_amount = bill_amount + tip_amount
amount_per_person = total_amount / num_people

print("\n--- Bill ---")
print(f"Original Bill Amount:", bill_amount)
print(f"Service Quality: {service_quality.capitalize()} ({tip_percentage * 100:.0f}% tip)")
print(f"Tip Amount: ", tip_amount)
print(f"Total Amount (Including Tip):", total_amount)
print(f"Number of People Splitting the Bill: ", num_people)
print(f"Amount Per Person: ", amount_per_person)
