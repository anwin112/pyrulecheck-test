import os
import sqlite3
from database import get_connection
from utils import calculate_sum

SECRET_KEY = "12345ABCDEF"  # Hardcoded secret

def login(username, password):
    conn = get_connection()
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
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
