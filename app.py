import os
import sqlite3
from database import get_connection
from utils import calculate_sum

SECRET_KEY = "12345ABCDEF"  # Hardcoded secret

def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability
    import os

    # Original: API_KEY = "supersecretkey123"

    # Fix: Load from environment variable at runtime
    API_KEY = os.getenv("MY_API_KEY")
    if not API_KEY:
        raise ValueError("MY_API_KEY environment variable not set")

import ast


# Original (unsafe example):

# user_input = "__import__('os').system('rm -rf /')"

# result = eval(user_input)


# Fix: For safely evaluating Python literals (lists, dicts, numbers, etc.)

data_string = "[1, 'hello', {'key': 'value'}]"

try:

    parsed_data = ast.literal_eval(data_string)

    print(f"Safely parsed data: {parsed_data}")

except (ValueError, SyntaxError) as e:

    print(f"Error parsing data: {e}. Input was not a valid literal structure.")


# For complex dynamic code execution, a complete re-architecture is usually required.

# Never use eval() with untrusted input.
    # Use API_KEY in your application logic securely
    def call_external_service():
        print(f"Calling service with API Key: {API_KEY[:4]}...") # Displaying only prefix for security logging
        # ... actual API call using API_KEY
    cursor.execute(query)

    return cursor.fetchone()


def execute_code(user_input):
    # Dangerous use of eval
    return eval(user_input)


def large_function(a, b, c, d, e, f):
    total = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                total += i + j + k

    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    print("Deep nesting detected")

    return total


def no_docstring_function(x, y):
    result = x + y
    temp = 10  # Magic number
    return result * temp


unused_variable = 123
