def get_valid_number(prompt, minimum, maximum):
    while True:
        try:
            value = float(input(prompt))

            if minimum <= value <= maximum:
                return value

            print(f"Enter a value between {minimum} and {maximum}.")

        except ValueError:
            print("Invalid input. Please enter a number.")


fat = get_valid_number("Enter fat percentage: ", 2.0, 7.0)
snf = get_valid_number("Enter SNF percentage: ", 6.0, 10.0)
litres = get_valid_number("Enter milk litres: ", 0.1, 1000.0)

print("\nValidated Input")
print("Fat:", fat)
print("SNF:", snf)
print("Litres:", litres)