#!/usr/bin/python3
""" Module for 0-minoperations"""

def minOperations(n):
    if n <= 1:
        return 0
# Find prime factorization of n
    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            # Factor found, add to operations
            operations += divisor
            n //= divisor

        divisor += 1

    return operations
