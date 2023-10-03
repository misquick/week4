def computepay(hours, rate):
    if hours > 40:
       overall_pay = 40 * rate + ((hours - 40) * rate * 1.5)
    else:
        overall_pay = hours * rate
    return overall_pay
try:
    hours = int(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    if hours < 0 or rate < 0:
        print("Hours and rate must be positive")
    else:
        pay = computepay(hours, rate)
        print(f"Salary: {pay:.2f}")
except ValueError:
    print("Error, please enter numeric input.")
