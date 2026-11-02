# Milk Payment Calculation using Expressions

base_rate = 30.00
standard_fat = 3.5
standard_snf = 8.5

fat = 4.0
snf = 8.7
litres = 10

fat_difference = (fat - standard_fat) / 0.1
snf_difference = (snf - standard_snf) / 0.1

fat_adjustment = fat_difference * 0.40
snf_adjustment = snf_difference * 0.30

rate = base_rate + fat_adjustment + snf_adjustment
payment = rate * litres

print("Fat:", fat)
print("SNF:", snf)
print("Milk Rate:", round(rate, 2))
print("Total Payment:", round(payment, 2))