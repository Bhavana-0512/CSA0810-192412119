# Seasonal Milk Payment Calculator

from decimal import Decimal, ROUND_HALF_UP

STANDARD_FAT = Decimal("3.5")
STANDARD_SNF = Decimal("8.5")
BONUS_LIMIT = Decimal("500")
BONUS_RATE = Decimal("0.50")


def calculate_rate(fat, snf, month):
    if month in [4, 5, 6]:
        base_rate = Decimal("32.00")
        fat_step_value = Decimal("0.45")
    else:
        base_rate = Decimal("30.00")
        fat_step_value = Decimal("0.40")

    snf_step_value = Decimal("0.30")

    fat_adjustment = (
        (fat - STANDARD_FAT) / Decimal("0.1")
    ) * fat_step_value

    snf_adjustment = (
        (snf - STANDARD_SNF) / Decimal("0.1")
    ) * snf_step_value

    return base_rate + fat_adjustment + snf_adjustment


def calculate_ten_day_payment(records, month):
    total_litres = sum(
        (litres for fat, snf, litres in records),
        Decimal("0")
    )

    bonus = (
        BONUS_RATE
        if total_litres > BONUS_LIMIT
        else Decimal("0")
    )

    total_payment = Decimal("0")

    for fat, snf, litres in records:
        rate = calculate_rate(fat, snf, month)
        total_payment += (rate + bonus) * litres

    return (
        total_litres,
        total_payment.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    )


# Get input
month = int(input("Enter month number (1-12): "))
records = []

for day in range(1, 11):
    print(f"\nDay {day}")

    fat = Decimal(input("Enter fat percentage: "))
    snf = Decimal(input("Enter SNF percentage: "))
    litres = Decimal(input("Enter milk litres: "))

    records.append((fat, snf, litres))

total_litres, payment = calculate_ten_day_payment(records, month)

print("\n--- Ten-Day Payment Summary ---")
print("Total Litres:", total_litres)
print("Total Payment: Rs.", payment)

if total_litres > BONUS_LIMIT:
    print("Bonus Applied: Rs. 0.50 per litre")
else:
    print("Bonus: Not Applied")