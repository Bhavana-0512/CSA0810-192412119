# Performance Analysis of Milk Payment Calculator

import time
import sys


def calculate_payments(farmers):
    total_payment = 0.0

    for farmer in farmers:
        fat, snf, litres = farmer

        fat_adjustment = ((fat - 3.5) / 0.1) * 0.40
        snf_adjustment = ((snf - 8.5) / 0.1) * 0.30

        rate = 30.00 + fat_adjustment + snf_adjustment
        total_payment += rate * litres

    return total_payment


# Test with different farmer counts
for count in [300, 6000, 150000]:
    farmers = [(4.0, 8.7, 10.0)] * count

    start_time = time.perf_counter()
    total = calculate_payments(farmers)
    end_time = time.perf_counter()

    print("\nFarmers:", count)
    print("Total Payment: Rs.", round(total, 2))
    print("Execution Time:", round(end_time - start_time, 6), "seconds")
    print("Memory Used:", sys.getsizeof(farmers), "bytes")