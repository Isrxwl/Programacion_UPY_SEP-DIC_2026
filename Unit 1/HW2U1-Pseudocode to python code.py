# Problem 1 — BMI Calculator
# INPUT
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))

# PROCESS
bmi = weight / (height ** 2)

# OUTPUT
print(f"Your Body Mass Index is: {bmi:.2f}")

# Problem 2 — Weekly Salary
# INPUT
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))

# PROCESS
salary = hours_worked * hourly_rate

# OUTPUT
print(f"Your weekly salary is: {salary:.2f}")

# Problem 3 — Final Price with Discount and VAT
# INPUT
price = float(input("Enter original price: "))
discount_rate = float(input("Enter discount rate (Ex. 0.20): "))

# PROCESS
discounted_price = price - (price * discount_rate)
total = discounted_price * 1.16

# OUTPUT
print(f"The final price after discount and VAT is: {total:.2f}")

# Problem 4 — Currency Conversion
# INPUT
amount_MXN = float(input("Enter amount in MXN: "))
exchange_rate_USD = float(input("Enter USD exchange rate: "))
exchange_rate_EUR = float(input("Enter EUR exchange rate: "))

# PROCESS
usd = amount_MXN / exchange_rate_USD
eur = amount_MXN / exchange_rate_EUR

# OUTPUT
print(f"Amount in USD: {usd:.2f}")
print(f"Amount in EUR: {eur:.2f}")

# Problem 5 — Grade Average
# INPUT
grade1 = float(input("Enter grade 1: "))
grade2 = float(input("Enter grade 2: "))
grade3 = float(input("Enter grade 3: "))

# PROCESS
average = (grade1 + grade2 + grade3) / 3

# OUTPUT
print(f"The average grade is: {round(average, 2)}")


