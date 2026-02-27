import os
import pickle
from app import login  # Circular import risk


def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


def unsafe_deserialization(data):
    # Unsafe pickle usage
    return pickle.loads(data)


def run_system_command(cmd):
    import subprocess
    subprocess.call(cmd, shell=True)  # Command injection risk


global_list = []


def append_global(item):
    global_list.append(item)
