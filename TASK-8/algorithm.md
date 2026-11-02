Task 8 – Milk Payment Calculator Algorithm

Objective

To calculate the payment for milk supplied by farmers based on fat percentage, SNF percentage, and quantity of milk.

Algorithm

1. Start the program.
2. Set the base milk rate to Rs. 30 per litre.
3. Set standard fat to 3.5% and standard SNF to 8.5%.
4. Get fat percentage, SNF percentage, and milk quantity as input.
5. Calculate the fat difference from the standard fat.
6. Calculate the SNF difference from the standard SNF.
7. Calculate fat adjustment: each 0.1% difference changes the rate by Rs. 0.40.
8. Calculate SNF adjustment: each 0.1% difference changes the rate by Rs. 0.30.
9. Add both adjustments to the base rate.
10. Multiply the calculated milk rate by the number of litres.
11. Display the milk rate and total payment.
12. Stop the program.

Formula

Fat Adjustment = ((Fat - 3.5) / 0.1) × 0.40

SNF Adjustment = ((SNF - 8.5) / 0.1) × 0.30

Milk Rate = 30 + Fat Adjustment + SNF Adjustment

Total Payment = Milk Rate × Litres

Example

Input:

- Fat = 4.0%
- SNF = 8.7%
- Milk = 10 litres

Output:

- Milk Rate = Rs. 32.10
- Total Payment = Rs. 321.00

Conclusion

The algorithm calculates milk payment using fat and SNF quality adjustments. It provides a systematic method for calculating farmer payments.