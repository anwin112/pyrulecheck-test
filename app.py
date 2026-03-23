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

    # Instead of: api_key = "my_hardcoded_secret_123"
    API_KEY = os.environ.get("MY_API_KEY")
    if not API_KEY:
        raise ValueError("Environment variable MY_API_KEY not set. Please configure it.")
    cursor.execute(query)

    import ast
    import json

    user_input = "{'name': 'Alice', 'age': 30}" # Example string that might be user-controlled

    # Safer alternative for evaluating Python literal structures (e.g., dicts, lists)
    try:
        data = ast.literal_eval(user_input)
        # Process 'data' safely, e.g., data['name']
    except (ValueError, SyntaxError) as e:
        print(f"Error evaluating input as literal: {e}")
        # Handle error appropriately (e.g., return 400 Bad Request)

    # If input is expected to be JSON, use json.loads
    # user_input_json = '{"product": "Laptop", "price": 1200}'
    # try:
    #     data = json.loads(user_input_json)
    #     # Process 'data' safely
    # except json.JSONDecodeError as e:
    #     print(f"Error decoding JSON input: {e}")
    #     # Handle error appropriately


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
