# Milk Rate Module

def calculate_milk_rate(fat, snf):
    base_rate = 30.00
    standard_fat = 3.5
    standard_snf = 8.5

    fat_adjustment = ((fat - standard_fat) / 0.1) * 0.40
    snf_adjustment = ((snf - standard_snf) / 0.1) * 0.30

    return round(base_rate + fat_adjustment + snf_adjustment, 2)