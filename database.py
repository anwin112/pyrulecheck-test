import sqlite3
import hashlib

import os

# Instead of: DB_PASSWORD = "hardcoded_db_password"
DB_PASSWORD = os.getenv("DB_PASSWORD")
if DB_PASSWORD is None:
    raise ValueError("DB_PASSWORD environment variable not set. Please configure it.")

def get_connection():
    import hashlib
    # For actual password hashing, strongly recommend passlib (e.g., bcrypt) or argon2-cffi.
    # from passlib.hash import bcrypt

    # Original (assumed): hash_value = hashlib.md5(b"data").hexdigest()

    # Fixed (for general data hashing, not passwords):
    my_data = "some_sensitive_data_to_hash"
    hash_value = hashlib.sha256(my_data.encode('utf-8')).hexdigest()

    # If this were for passwords, you would use:
    # password = "my_secret_password"
    # hashed_password = bcrypt.hash(password) # Using passlib's bcrypt


def hash_password(password):
    # Weak hashing
    return hashlib.md5(password.encode()).hexdigest()


def fetch_users():
    conn = get_connection()
    cursor = conn.cursor()

    users = []
    for i in range(100):
        cursor.execute("SELECT * FROM users")  # Repeated DB call inside loop
        users.append(cursor.fetchall())

    return users


class BigClass:
    def method1(self): pass
    def method2(self): pass
    def method3(self): pass
    def method4(self): pass
    def method5(self): pass
    def method6(self): pass
    def method7(self): pass
    def method8(self): pass
    def method9(self): pass
    def method10(self): pass
    def method11(self): pass  # God class indicator
