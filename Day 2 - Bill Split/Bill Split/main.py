print("Bill Calculator!")
total_bill = float(input("What was the total bill? $"))
tip_value = float(input("How much tip? 10, 12 or 15? "))
number_of_people = float(input("How many people are splitting the bill? "))

print(
    f"Each person should pay: ${(total_bill + total_bill*(tip_value/100))/number_of_people}")
