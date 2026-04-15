# Function to add two numbers
def addNumbers(x, y):
    return x + y

# Function to subtract two numbers
def subtractNumbers(x, y):
    return x - y

# Function to calculate (a + b) - c
def calculate(a, b, c):
    sum_result = addNumbers(a, b)
    final_result = subtractNumbers(sum_result, c)
    return final_result

# Example usage
result = calculate(2, 3, 4)
print("Result:", result)  # Output: 1
