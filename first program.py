def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def is_palindrome(num):
    num_str = str(num)
    reversed_str = num_str[::-1]
    return num_str == reversed_str

num = int(input("Enter an integer: "))

if num % 2 != 0:  # Odd number
    fact = factorial(num)
    digit_count = len(str(fact))
    print(f"The factorial of {num} is: {fact}")
    print(f"The number of digits in the factorial of {num} is: {digit_count}")
else:  # Even number
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
