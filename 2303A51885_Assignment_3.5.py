#write a code to check whether the given year is leap year or not.
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap_year(2020))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(2021))  # False

"""
Input: 12, 18 → Output: 6
"""
"""def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(12, 18))  # 6
print(gcd(100, 75))  # 25
print(gcd(7, 3))    # 1
"""
"""• Input: 4, 6 → Output: 12
• Input: 5, 10 → Output: 10
• Input: 7, 3 → Output: 21
"""
def lcm(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return a * b // gcd(a, b)
print(lcm(4, 6))   # 12
print(lcm(5, 10))  # 10
print(lcm(7, 3))   # 21