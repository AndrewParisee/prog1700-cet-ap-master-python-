"""
Write code that creates a 5x5 matrix and fills the matrix with random numbers between 1 - 100.
from random import randint
"""
import random

matrix = []
file_name = "Matrix.csv"
access_mode = "w"

for other_steps in range(5):
    row = []
    for steps in range(5):
        num = random.randint(1, 100)
        row.append(num)
        # file_handle.write(str(num) + ",")
    matrix.append(row)
    # file_handle.write("\n")

with open(file_name,access_mode) as file_handle:
    for row in matrix:
        for index in range(len(row)):
            if index == 4:
                file_handle.write(str(row[index]))
            else:
                file_handle.write(str(row[index]) + ",")
        file_handle.write("\n")

