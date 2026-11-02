# Milk Payment Calculator using Functions

def calculate_milk_rate(fat, snf):
    base_rate = 30.00
    standard_fat = 3.5
    standard_snf = 8.5

    fat_adjustment = ((fat - standard_fat) / 0.1) * 0.40
    snf_adjustment = ((snf - standard_snf) / 0.1) * 0.30

    rate = base_rate + fat_adjustment + snf_adjustment
    return round(rate, 2)


def calculate_payment(rate, litres):
    return round(rate * litres, 2)


# Sample input
fat = 4.0
snf = 8.7
litres = 10

rate = calculate_milk_rate(fat, snf)
payment = calculate_payment(rate, litres)

print("Fat:", fat)
print("SNF:", snf)
print("Milk Rate:", rate)
print("Total Payment:", payment)