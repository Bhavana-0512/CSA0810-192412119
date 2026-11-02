TASK 2 – Explore Values and Types in the Interpreter

1. Python Data Types

Python provides different data types to store different kinds of values.

- 10 – int: Stores whole numbers.
- 10.0 – float: Stores decimal numbers.
- "10" – str: Stores text values.
- True – bool: Stores Boolean values (True or False).
- [10, 8.5] – list: Stores multiple values in a single variable.

The type() function is used to identify the data type of a value.

2. Arithmetic Operators

Python supports different arithmetic operators.

- 7 / 2 = 3.5: Normal division returns a float value.
- 7 // 2 = 3: Floor division returns the quotient rounded down.
- 7 % 2 = 1: Modulus returns the remainder.
- -7 // 2 = -4: Floor division rounds towards negative infinity.

These operators are useful for performing calculations in the milk payment system.

3. Floating-Point Precision

The expression 0.1 + 0.2 == 0.3 returns False.

This happens because computers store floating-point numbers in binary format. Some decimal values cannot be represented exactly in binary, resulting in small precision errors.

Therefore, float values may produce unexpected results in financial calculations.

4. Money Calculation

Float is not recommended for financial calculations because it may produce small rounding errors.

The following alternatives can be used:

- Decimal module: Provides accurate decimal arithmetic when values are created directly from strings.
- Integer paise: Stores money as whole paise. For example, Rs 33.40 is stored as 3340 paise.
- round(): Rounds a numerical result to a specified number of decimal places, but does not eliminate all floating-point errors.

Decimal and integer paise are suitable choices for accurate money calculations.

5. Decimal Program Explanation

The decimal_test.py program calculates the total of 1000 payments of Rs 33.40 and three adjustments of Rs 0.10.

The total_float() function uses float values to calculate the total.

The total_decimal() function uses Decimal values created directly from strings to calculate the total accurately.

The float result contains a small precision error, whereas the Decimal result is Rs 33400.30.

This demonstrates why Decimal is more suitable for financial calculations.

6. Decimal from Float

When Decimal(amount) is used, the amount is converted directly from a string into Decimal. This preserves the exact decimal value represented by the string.

When Decimal(float(amount)) is used, the float value is converted into Decimal. Since float may already contain binary precision errors, those errors are preserved in the Decimal result.

Therefore, Decimal should be created directly from strings instead of converting through float.

7. Alternative Concept and Complexity Analysis

There are three possible methods for calculating the total payment.

Method 1: Float

Float can be used to add payment values. However, it may produce small precision errors.

Method 2: Decimal

Decimal provides accurate decimal arithmetic and is suitable for financial calculations.

Method 3: Integer Paise

Money can be converted into paise and stored as integers. For example, Rs 33.40 becomes 3340 paise. This method provides exact whole-paise calculations.

Time and Space Complexity

- Float: O(n) time and O(1) auxiliary space.
- Decimal: O(n) time and O(1) auxiliary space.
- Integer Paise: O(n) time and O(1) auxiliary space.

Here, n represents the number of payments. Each method processes every payment once and maintains a running total.

The size of individual numerical values can be checked using sys.getsizeof().

8. Conclusion

Python provides different data types and arithmetic operators for performing calculations. Floating-point values may produce precision errors, which can affect financial calculations.

Decimal and integer paise provide more reliable methods for calculating farmer payments. Therefore, Decimal is recommended for the village milk co-operative payment calculator.