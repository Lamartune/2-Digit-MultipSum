num1 = input("Enter the first 2-digit positive integer number: ")
num2 = input("Enter the second 2-digit positive integer number: ")

# Calculate sum of individual digits of first number
digit_sum1 = int(num1[0]) + int(num1[1])

# Calculate multiplication of individual digits of second number
digit_mul2 = int(num2[0]) * int(num2[1])

# Calculate sum of the above two results
result = digit_sum1 + digit_mul2

# Output the final result
print("Result:", result)