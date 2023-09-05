# 1. What is the following output of the python code given below:
data = [10,501,22,37,100,999,87,351]
result = filter(lambda x: x > 4, data)
print(list(result)) # Output =[10,501,22,37,100,999,87,351]

# 2.Write a python program using lambda function to check whether every element of a list is an integer or string.
my_list = [19, "guvi", 3.14, "shiv", 7]

is_string = lambda item: isinstance(item, str)
is_integer = lambda item: isinstance(item, int)
string_check = list(map(is_string, my_list))
integer_check = list(map(is_integer, my_list))

# Print the results
for item, is_str, is_int in zip(my_list, string_check, integer_check):
    if is_str:
        print(f"'{item}' is a string.")
    elif is_int:
        print(f"{item} is an integer.")
    else:
        print(f"{item} is of another data type.")



#3. Write  a program on fibonacci series using lambda function from elements 1 to 50
from functools import reduce

# Definlambdae a  function to generate the Fibonacci sequence
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [1, 1])

n = 50  # The number of Fibonacci numbers to generate
fibonacci_sequence = fibonacci(n)

# Filter the Fibonacci numbers greater than or equal to 1
filtered_fibonacci_sequence = list(filter(lambda x: x <50, fibonacci_sequence))

print(filtered_fibonacci_sequence)

# 4. Write a python function to validate the Regular expression.
# a). Email address b) MObile number of Bangladesh  c)Telephone number of USA d)Password
import re
def validate_pattern(pattern, input_string):

    # Use the re.match() function to check if the input string matches the pattern
    if re.match(pattern, input_string):
        return True
    else:
        return False

# a) Email Address
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
email_input = 'example@email.com'
print("Is Email Valid:", validate_pattern(email_pattern, email_input))

# b) Mobile Number of Bangladesh (Assuming a common format)
bangladesh_mobile_pattern = r'^\+8801[0-9]{9}$'
bangladesh_mobile_input = '+8801712345678'
print("Is Bangladesh Mobile Number Valid:", validate_pattern(bangladesh_mobile_pattern, bangladesh_mobile_input))

# c) Telephone Number of USA (Assuming a common format)
usa_telephone_pattern = r'^\(\d{3}\)\s?\d{3}-\d{4}$'
usa_telephone_input = '(123) 456-7890'
print("Is USA Telephone Number Valid:", validate_pattern(usa_telephone_pattern, usa_telephone_input))

# d) Password (Assuming at least 8 characters, including letters, numbers, and special characters)
password_pattern = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$'
password_input = 'Password@1234567'
print("Is Password Valid:", validate_pattern(password_pattern, password_input))




