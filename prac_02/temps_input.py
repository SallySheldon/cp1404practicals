"""
CP1404 - Prac 02 - Extension - More temperatures
Program to generate temps for .txt file
"""

import random

NUMBER_OF_TEMPERATURES = 20

out_file = open("temps_input.txt", "w")
for i in range(NUMBER_OF_TEMPERATURES):
    temperature = random.uniform(-200, 200)
    print(temperature, file=out_file)
out_file.close()
