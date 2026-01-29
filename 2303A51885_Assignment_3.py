#Write a code for checking palindrome number
def is_palindrome(number):
    # Convert the number to string
    str_num = str(number)
    # Check if the string is equal to its reverse
    return str_num == str_num[::-1]
print(is_palindrome(121))  # True
print(is_palindrome(-121)) # False
print(is_palindrome(10))   # False
print(is_palindrome(12321)) # True

"""
Input: 5 → Output: 120
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
print(factorial(6))  # Output: 720

"""
Input: 153 → Output: Armstrong Number
Input: 370 → Output: Armstrong Number
Input: 123 → Output: Not an Armstrong Number
"""
def is_armstrong(number):
    # Convert the number to string to easily iterate over digits
    str_num = str(number)
    num_digits = len(str_num)
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    return sum_of_powers == number
print(is_armstrong(153))  # True
print(is_armstrong(123))  # False
print(is_armstrong(9474)) # True



"""
23 → Output: Prime Number
24 → Output: Composite Number
1 → Output: Neither
-1 → Output: enter valid number
abc → Output: enter valid number
1.5 → Output: enter valid number
"""
def check_prime_composite(number):
    if not isinstance(number, int) or number < 1:
        return "enter valid number"
    if number == 1:
        return "Neither"
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return "Composite Number"
    return "Prime Number"   
print(check_prime_composite(23))  # Output: Prime Number
print(check_prime_composite(24))  # Output: Composite Number
print(check_prime_composite(1))   # Output: Neither
print(check_prime_composite(-1))  # Output: enter valid number
print(check_prime_composite("abc"))  # Output: enter valid number
print(check_prime_composite(1.5))  # Output: enter valid number

#Write a code for perfect number
def is_perfect_number(number):
    if number < 1:
        return False
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    return divisors_sum == number
print(is_perfect_number(6))   # True
print(is_perfect_number(28))  # True
print(is_perfect_number(12))  # False

"""
•	Input: 8 → Output: Even
•	Input: 15 → Output: Odd
•	Input: 0 → Output: Even

"""
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(8))   # Output: Even
print(check_even_odd(15))  # Output: Odd
print(check_even_odd(0))   # Output: Even
print(check_even_odd(-4))  # Output: Even