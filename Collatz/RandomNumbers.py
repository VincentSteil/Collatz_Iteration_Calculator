"""
Vincent Steil
30/01/2013

to run the program:
python RandomNumbers.py > vjs432-RunCollatz.in  

"""
import sys, random


def generate_numbers(n):
    random.seed()
    for x in xrange(0, n+1) :
        sys.stdout.write(str(random.randint(1, 10000)) + " " + str(random.randint(1, 1000)) + "\n")

generate_numbers(1000)