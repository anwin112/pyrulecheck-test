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

    # Instead of: API_KEY = "your_hardcoded_api_key"
    API_KEY = os.getenv("APP_API_KEY")
    if API_KEY is None:
        raise ValueError("APP_API_KEY environment variable not set. Please configure it.")
    cursor.execute(query)

    import ast

    # Original (assumed): result = eval(user_input)

    # Fixed (for safe literal/data structure evaluation):
    user_input_string = "{"key": "value", "number": 123}"
    try:
        safe_data = ast.literal_eval(user_input_string)
        # Process safe_data (e.g., dictionary, list, number)
    except (ValueError, SyntaxError) as e:
        # Handle invalid input gracefully without evaluating code
        print(f"Invalid input received, cannot safely evaluate: {e}")
        safe_data = None


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
