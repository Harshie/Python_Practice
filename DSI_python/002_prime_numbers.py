# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 21:17:53 2020

@author: ehars
"""

# Finding the prime numbers from the list
#n = 20
n = 100000
number_range = set(range(2,n+1))
#print(number_range)

prime_number_list = []

while number_range:
    prime = number_range.pop()
    prime_number_list.append(prime)
    multiples = set(range(prime*2,n+1,prime))
    number_range.difference_update(multiples)

print(prime_number_list)
count = len(prime_number_list)
largest = max(prime_number_list)
print(f"There are {count} prime number between 2 and {n} and the largest prime number is {largest}")