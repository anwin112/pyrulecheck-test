import sqlite3
import hashlib

DB_PASSWORD = "mypassword"  # Hardcoded secret

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
