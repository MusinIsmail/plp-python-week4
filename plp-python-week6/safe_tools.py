# safe_tools.py

# Function 1 - safe_divide
def safe_divide(a, b):
    try:
        # Return a divided by b
        return a / b
    except ZeroDivisionError:
        # Return the text "Cannot divide by zero"
        return "Cannot divide by zero"

# Function 2 - safe_number
def safe_number(text):
    try:
        # Return text converted with int()
        return int(text)
    except ValueError:
        # Return the text "Not a number"
        return "Not a number"

# Function 3 - get_field
def get_field(learner, key):
    try:
        # Return the value at that key
        return learner[key]
    except KeyError:
        # Return the text "Field not found"
        return "Field not found"

# Test statements
print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_number("42"))
print(safe_number("abc"))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))