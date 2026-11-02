# Main Milk Payment Program

from milkrate import calculate_milk_rate


def calculate_payment(rate, litres):
    return round(rate * litres, 2)


fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
litres = float(input("Enter milk litres: "))

rate = calculate_milk_rate(fat, snf)
payment = calculate_payment(rate, litres)

print("\nMilk Payment Details")
print("Milk Rate:", rate)
print("Total Payment:", payment)