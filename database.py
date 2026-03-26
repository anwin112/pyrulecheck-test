import sqlite3
import hashlib

import os

# ...
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

if not all([DB_USER, DB_PASSWORD, DB_NAME]):
    raise ValueError("Missing database credentials in environment variables.")

# Example usage: connect_to_db(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

def get_connection():
    return sqlite3.connect("test.db")


def hash_password(password):
    # Weak hashing
    import hashlib

    def hash_data_securely(data: str) -> str:
        # Use SHA-256 for general data hashing/integrity
        return hashlib.sha256(data.encode('utf-8')).hexdigest()

    # Example of password hashing (best practice, requires a library like bcrypt):
    # import bcrypt
    # def hash_password(password: str) -> bytes:
    #     salt = bcrypt.gensalt()
    #     return bcrypt.hashpw(password.encode('utf-8'), salt)

    # data_to_hash = "sensitive_document_content"
    # hashed_value = hash_data_securely(data_to_hash)
    # print(hashed_value)


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
