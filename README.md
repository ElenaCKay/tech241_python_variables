# Intro to Python

## Variables
Python is a dynamically typed language so you do not state data types. 
Variables can be changed and overwritten. The hash key creates comments.
```python
a = 1
b = 2
c = 3.5
hi = "My name is Elena"

print(a + b)
# 3
```
## Methods

The `type()` method will take a variable as a parameter and give the variable type as a response.

The `print()` method prints code into the terminal (like console.log())

## Data types

There are three main data types:

1. Numbers -> Floats, ints, complex, longs
2. Strings -> Anything surrounded by quotation marks " " or  ' '
3. Booleans -> True or False

### Operators

There are arithmetic operators:
+, -, /, *, %

And there are comparison operators:
<, >, ==, <=, >=, !=

### Strings

They can use single and double quotes. To slice a string you can use square brackets with a colon.
Do not forget that strings are 0 indexed.

```python
hi = "Hello world!"
print(hi[-6:]) # "world!"
print(hi[0:5]) # "Hello"
```
#### String method examples:

- len() -> length of the string / array
- strip() -> gets rid of whitespace at the end of a string
- .lower() -> makes it lowercase
- .upper() -> makes it uppercase
- .capitilise() -> capitilises every word
- .count() -> counts the characters in the paranthesis
- .replace("what you want to replace", "What you are replacing with") -> replaces a character with somthing else

Concatination -> Adding the **same** data type together (string + string)

Casting -> Adding two **different** data types together

Int to string example:
```python
x = 2
y = 4.5
z = "I am a string"

print(str(x) + " " + str(y) + " " + z)

# 2 4.5 I am a string
```
String to numeric example:
```python
int_string = "6"
print(type(int(int_string)))
#'int'
```

### F-Strings (Formatted strings)

Formatted strings have f before the start of the string and they use curly brackets to input variables. It is very similar to backticks in JavaScript.

```python
name = "lassie"
years = 7
height_cm = 60.2
print(f"{name.capitalize()} is {years * 7} years old in dog years")
# Lassie is 49 years old in dog years

pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi:.3f}")
# Pi to 3 decimal places: 3.142

# percentages

score = 16
max_score = 26

print(f"you scored {score/max_score:.2%}")
# you scored 61.54%
```

### Booleans

Booleans are a True or False value. The capitalisation is very important.
They are used with the comparison operators for example:

```python
a = True
b = False

print(a == b) # False
print(a != b) # True

print(a >= True) # True
print(b <= False)  # True
```
### Keywords

There are two main key words: and, or. These are used to check if two or more values are true or false.
For example:
```python
print(True and False) # False
print(True and True) # True
print(True or False) # True
```
### Booleans with data types

There are many methods which use booleans as an answer.
 ```python
 hi = "Hello world!"

print(hi.isalpha()) # False checks that there are only letters
print(hi.islower()) # False checks if the string is lowercase
print(hi.endswith("!")) # True checks if something endswith something#
print(hi.startswith("H")) # True
 ```
0 is a falsy value and so will always be False when any methods are used on it.

### Value of None

None is not nothing and not 0. It is neither true nor false. It is just a placeholder.
To check if something is None you can use the == however this is not recommended as it uses booleons and this may confuse the programme.
To do it correctly you should use the term is. For example:

```python
x = None
print(x is None)
# True
```