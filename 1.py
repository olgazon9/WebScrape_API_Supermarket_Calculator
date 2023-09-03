import logging

# Configure logging
logging.basicConfig(filename='operations.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add_numbers(a, b):
    result = a + b
    logging.info(f"Added {a} and {b}, result: {result}")
    return result

def subtract_numbers(a, b):
    result = a - b
    logging.info(f"Subtracted {b} from {a}, result: {result}")
    return result

def multiply_numbers(a, b):
    result = a * b
    logging.info(f"Multiplied {a} by {b}, result: {result}")
    return result

def divide_numbers(a, b):
    if b != 0:
        result = a / b
        logging.info(f"Divided {a} by {b}, result: {result}")
        return result
    else:
        logging.error("Division by zero attempted")
        raise ValueError("Cannot divide by zero")

# Get user input for numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_result = add_numbers(num1, num2)
subtraction_result = subtract_numbers(num1, num2)
multiplication_result = multiply_numbers(num1, num2)

try:
    division_result = divide_numbers(num1, num2)
    print(f"Division: {division_result}")
except ValueError as e:
    print(e)

print(f"Sum: {sum_result}")
print(f"Difference: {subtraction_result}")
print(f"Product: {multiplication_result}")
