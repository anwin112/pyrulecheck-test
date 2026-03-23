import sqlite3
import hashlib

import os

# Original: DB_PASSWORD = "mysecretpass"

# Fix: Load from environment variable
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
if not DB_PASSWORD:
    raise ValueError("DATABASE_PASSWORD environment variable not set")

import hashlib

import bcrypt # Requires 'pip install bcrypt' for password hashing


# Original (unsafe example):

# data = b"sensitive_data"; hashed_data = hashlib.md5(data).hexdigest()


# Fix: For general data integrity hashing, use SHA256

file_content = b"important_document_content"

hashed_content_sha256 = hashlib.sha256(file_content).hexdigest()

print(f"SHA256 Hash for content: {hashed_content_sha256}")


# Fix: For secure password storage, use bcrypt

user_password = b"mysecretpassword123"

# Generate a unique salt for each password

salt = bcrypt.gensalt()

# Hash the password with the salt

hashed_password_bcrypt = bcrypt.hashpw(user_password, salt)

print(f"Bcrypt Hashed Password: {hashed_password_bcrypt.decode()}")


# To verify a password later:

# stored_hash = b"...from_database..."

# user_supplied_password_attempt = b"user_input"

# if bcrypt.checkpw(user_supplied_password_attempt, stored_hash):

#     print("Password matches!")

# else:

#     print("Password does not match.")
# Use DB_PASSWORD for database connection
def connect_to_database():
    print(f"Connecting to DB with user and obfuscated password: ********")
    # Example: db_connection = create_db_connection(user='admin', password=DB_PASSWORD)
    # ... actual database connection logic

def get_connection():
    return sqlite3.connect("test.db")


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
