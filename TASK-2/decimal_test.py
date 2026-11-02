from decimal import Decimal

# 1000 payments of Rs 33.40
# and three adjustments of Rs 0.10

payments = ["33.40"] * 1000 + ["0.10"] * 3


def total_float(items):
    total = 0.0

    for amount in items:
        total += float(amount)

    return total


def total_decimal(items):
    total = Decimal("0")

    for amount in items:
        total += Decimal(amount)

    return total


print("float :", total_float(payments))
print("Decimal:", total_decimal(payments))

print(
    0.1 + 0.2 == 0.3,
    Decimal("0.1") + Decimal("0.2") == Decimal("0.3")
)

# Decimal from float comparison
total_decimal_float = Decimal("0")

for amount in payments:
    total_decimal_float += Decimal(float(amount))

print("Decimal from float:", total_decimal_float)