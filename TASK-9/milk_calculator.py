# Milk Payment Calculator

BASE_RATE = 30.00
STANDARD_FAT = 3.5
STANDARD_SNF = 8.5
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30


def calculate_rate(fat, snf):
    fat_adjustment = ((fat - STANDARD_FAT) / 0.1) * FAT_STEP_VALUE
    snf_adjustment = ((snf - STANDARD_SNF) / 0.1) * SNF_STEP_VALUE

    return round(BASE_RATE + fat_adjustment + snf_adjustment, 2)


def calculate_payment(fat, snf, litres):
    rate = calculate_rate(fat, snf)
    payment = rate * litres
    return rate, round(payment, 2)


# Get farmer details
farmer_name = input("Enter farmer name: ")
fat = float(input("Enter fat percentage: "))
snf = float(input("Enter SNF percentage: "))
litres = float(input("Enter milk litres: "))

rate, payment = calculate_payment(fat, snf, litres)

print("\n--- Milk Payment Details ---")
print("Farmer Name:", farmer_name)
print("Milk Rate: Rs.", rate)
print("Milk Quantity:", litres, "litres")
print("Total Payment: Rs.", payment)