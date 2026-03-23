import sqlite3
import hashlib

import os

# Instead of: DB_PASSWORD = "super_secret_db_pass"
DB_PASSWORD = os.environ.get("DATABASE_PASSWORD")
if not DB_PASSWORD:
    raise ValueError("Environment variable DATABASE_PASSWORD not set. Please configure it.")

def get_connection():
    import hashlib
    import os
    # Install passlib for robust KDFs: pip install passlib
    # from passlib.hash import argon2

    # For general-purpose data integrity (e.g., file checksums):
    data_to_hash = b"sensitive_data_example"
    # Instead of: hashlib.md5(data_to_hash).hexdigest()
    secure_hash_sha256 = hashlib.sha256(data_to_hash).hexdigest()

    # For password storage (HIGHLY RECOMMENDED, do NOT use hashlib directly for passwords):
    # password = "my_secure_password"
    # hashed_password = argon2.hash(password)
    # To verify: argon2.verify(input_password, stored_hashed_password)


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
