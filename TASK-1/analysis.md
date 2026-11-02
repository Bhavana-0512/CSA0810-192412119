# TASK 1 – Understand the Problem and Identify the Data

## 1. Introduction

The Ksheera Village Milk Co-operative collects milk from farmers twice a day. The payment depends on the quantity of milk, fat percentage and SNF percentage.

The program calculates the rate per litre and the total amount payable to each farmer for ten days.

## 2. Problem Analysis

The main objective is to calculate the correct payment for every farmer based on milk quantity, fat percentage and SNF percentage.

The system must calculate the rate per litre, individual payment and ten-day total payment accurately.

## 3. Inputs

The following inputs are required for the milk payment calculator.

| Input | Data Type | Description |
|---|---|---|
| Farmer ID | String | Unique identification of the farmer |
| Litres | Float | Quantity of milk supplied |
| Fat | Float | Fat percentage of milk |
| SNF | Float | Solids-not-fat percentage |
| Shift | String | Morning or Evening shift |

### Justification

- Farmer ID is a string because it may contain letters and numbers.
- Litres is a fractional value because milk quantity can be measured in decimal values.
- Fat and SNF are floating-point values because percentages may contain decimal values.
- Shift is a string because it represents Morning or Evening.

## 4. Outputs

| Output | Data Type | Description |
|---|---|---|
| Rate per litre | Decimal | Calculated milk rate |
| Payment amount | Decimal | Amount payable for each entry |
| Ten-day total | Decimal | Total payment for ten days |

### Justification

Decimal is suitable for monetary calculations because it provides accurate decimal arithmetic and avoids floating-point errors.

## 5. Constants

The following values remain unchanged during one calculation run.

| Constant | Value | Purpose |
|---|---:|---|
| BASE_RATE | 30.00 | Basic rate per litre |
| STANDARD_FAT | 3.5 | Standard fat percentage |
| STANDARD_SNF | 8.5 | Standard SNF percentage |
| FAT_STEP | 0.1 | Fat calculation step |
| SNF_STEP | 0.1 | SNF calculation step |
| FAT_STEP_VALUE | 0.40 | Value for each fat step |
| SNF_STEP_VALUE | 0.30 | Value for each SNF step |

These values are defined as constants to avoid changing the same values in multiple places.

## 6. Rules and Validation

The following rules must be satisfied:

1. Milk quantity must be greater than zero.
2. Fat percentage must be between 2.0% and 7.0%.
3. SNF percentage must be a valid numerical reading within the range specified by the milk analyser or co-operative.
4. Farmer ID must not be empty.
5. Shift must be either Morning or Evening.
6. Negative values are not accepted.
7. The payment must be rounded to two decimal places.
8. Every 0.1% increase or decrease in fat changes the rate by Rs 0.40.
9. Every 0.1% increase or decrease in SNF changes the rate by Rs 0.30.

## 7. Assumptions

1. Each farmer supplies milk twice a day.
2. The payment is calculated for every ten-day period.
3. The standard fat percentage is 3.5%.
4. The standard SNF percentage is 8.5%.
5. Each farmer has a unique identification number.
6. The rate is calculated using fat and SNF values.
7. All monetary calculations must be accurate to the nearest paisa.
8. The accepted SNF range will follow the co-operative's analyser specification.

## 8. Alternative Concept and Complexity Analysis

### Method 1: Separate Variables

If separate variables such as litres1, fat1 and snf1 are used for each farmer, many variables are required.

For 300 farmers, 900 variables are needed for these three values alone.

Example:

```python
litres1 = 10.0
fat1 = 3.5
snf1 = 8.5

litres2 = 8.0
fat2 = 4.0
snf2 = 8.7
```

This method becomes difficult to maintain when the number of farmers increases.

### Method 2: List of Tuples

Instead of separate variables, a list of tuples can store the details of all farmers.

Example:

```python
entries = [
    (10.0, 3.5, 8.5),
    (8.0, 4.0, 8.7),
    (12.0, 3.2, 8.3)
]
```

Each tuple stores the litres, fat and SNF values of one entry.

### Complexity Comparison

| Comparison | Separate Variables | List of Tuples |
|---|---|---|
| Time Complexity | O(n) | O(n) |
| Space Complexity | O(n) | O(n) |
| Maintenance | Difficult | Easy |
| Scalability | Poor | Better |

Both methods require O(n) time to process n entries and O(n) space to store them.

However, a list of tuples is easier to manage, access, update and process when the number of farmers increases from 300 to 150,000.

## 9. Conclusion

A list of tuples is selected to store farmer entries because it is simple, organised and scalable.

Decimal is selected for monetary calculations to maintain accuracy up to two decimal places.

Named constants are used to make future rate revisions easier and avoid errors.