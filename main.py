# /*
#  * * DO NOT ALTER OR REMOVE COPYRIGHT NOTICES OR THIS FILE HEADER.
#  * *
#  * * Copyright (C) 2023 Fatih Tün - All Rights Reserved
#  * *
#  * * Unauthorized copying of this file, via any medium is strictly prohibited
#  * *
#  * * Proprietary and confidental.
#  * *
#  * * Written by Fatih TÜN <tunbusiness1@gmail.com>, April 2023
#  */



# This program prompts the user to input two 2-digit positive integer numbers and 
# performs the following operations on them:
# 1. Calculates the sum of the individual digits of the first number.
# 2. Calculates the multiplication of the individual digits of the second number.
# 3. Calculates the sum of the above two results.
# 4. Outputs the final result.

# Prompt the user to input the two numbers.
num1 = input("Enter the first 2-digit positive integer number: ")
num2 = input("Enter the second 2-digit positive integer number: ")

# Calculate sum of individual digits of first number.
digit_sum1 = int(num1[0]) + int(num1[1])

# Calculate multiplication of individual digits of second number.
digit_mul2 = int(num2[0]) * int(num2[1])

# Calculate sum of the above two results.
result = digit_sum1 + digit_mul2

# Output the final result.
print("Result:", result)
