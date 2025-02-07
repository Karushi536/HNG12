"""Function to check if a number is prime or not.
:param n: int
"""
def isPrime(n):
    n = abs(n)
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

perfect_numbers = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]
"""Function to check if a number is perfect or not."""
def isPerfect(n):
    n = abs(n)
    if n in perfect_numbers:
        return True
    return False

"""Function to calculate the sum of digits of a number."""
def digit_sum(n):
    n = abs(n)
    return sum([int(i) for i in str(n)])

"""
Function to check the properties of a number.
:param n: int
"""
def check_number_properties(n):
    def is_armstrong(num):
        num = abs(num)
        digits = [int(d) for d in str(num)]
        power = len(digits)
        return num == sum(d ** power for d in digits)

    properties = []
    
    if is_armstrong(n):
        properties.append("armstrong")
    
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")
    
    return properties
