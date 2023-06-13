# Data types

# Numbers -> float, ints, complex, longs
# Strings -> characters or text
# Booleans -> True or False

# Operators

# Arithmetic operators

# +, -, /, *, %


# Comparision operators

# >, <, ==, <=, >=, !=

# Numeric types

# a = 24
# b = 16
#
# print(a + b) # 40
# print(a - b) # 8
# print(a / b) # 1.5
# print(a < b) # False
#
# floatNum = 1.356
# intNum = 4
# print(type(floatNum + intNum))

# one_third = 1 / 3
# print(one_third + 3)

# Strings

single_quotes = 'Look, single quotes'
double_quotes = "Look, double quotes"

# String slicing

# hi = "Hello world!"
# print(hi[-6:])
# print(hi[0:5])

# String methods

# len() -> length of the string / array
# strip() -> gets rid of whitespace at the end of a string
# .lower() -> makes it lowercase
# .upper() -> makes it uppercase
# .capitilise() -> capitilises every word
# .count() -> counts the characters in the paranthesis
# .replace("what you want to replace", "What you are replacing with") -> replaces a character with somthing else

#Concatination -> Adding two strings togther

# Casting -> adding two different types of data together

# x = 2
# y = 4.5
# z = "I am a string"
#
# print(str(x) + " " + str(y) + " " + z)
#
# # String to numeric
#
# int_string = "6"
#
# print(type(int(int_string)))

# F-Strings formatted strings
# Dont always need to cast

name = "lassie"
years = 7
height_cm = 60.2
print(f"{name.capitalize()} is {years * 7} years old in dog years")

pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi:.3f}")

# percentages

score = 16
max_score = 26

print(f"you scored {score/max_score:.2%}")



