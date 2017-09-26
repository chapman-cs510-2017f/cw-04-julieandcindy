#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Julie Gardner-Hoag, Cynthia Parks
# Student ID: 2299636, 2303535
# Email: gardnerh@chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 4
###

$ python
  >>> import primes
  >>> help(primes)

"""Primes
In this module we have a function, eratosthenes(n), that uses the Eratosthenes Sieve to produce a list of prime numbers.
The Eratosthenes Sieve removes multiples of primes, leaving behind all the prime numbers.  In our program we have the full
list of numbers up to n generate, then remove non primes from the list.  For example, if the user entered the number 10, 
the sieve would start with 2, then remove the numbers {4, 6, 8, 10}.  It would then move to the number 3, and proceed to 
remove {9}, since 6 had previously been removed.  Now our list contains {2, 3, 5, 7}. 

Additionally, this module contains the function gen_eratosthenes() that generates the next prime number each time it is 
implemented.
"""

def eratosthenes(n):
    """
    This function is titled eratosthenes(n) because it uses the Eratosthenes Sieve to produce a list of prime
    numbers.  It takes in one positive integer arguement, the returns a list of all the primes less than the 
    given number.
    
        Args:
            n (int): User input
        Returns:
            primes (list): List of prime numbers less than the user input
    """
    primes = []
    
    #checks for positive number
    if n<=0:
        print("Please enter a positive number")
        return
    
    #creates list of numbers up to n
    count = 2
    while count<=n-1:
        primes.append(count)
        count +=1
        
    p = 2
    
    #starts with 2, then removes all multiples of 2.  Moves to 3, removes
    #all multiples of 3, and so on until we have a list of prime numbers 
    #less than n.
    while p<=n:
        for i in range(2, n+1):
            if i*p <= n:
                #checks to see if the number was already removed from the list
                if i*p not in primes:
                    continue
                else:
                    primes.remove(i*p)
        p +=1
    
    return primes

def gen_eratosthenes():
    """
    This function is titled gen_eratosthenes() because it uses the eratosthenes sieve function to generate a new
    prime number each time it is implemented.  It does not take any inputs and returns a list of prime numbers.
    
        Args:
            none
        Yields:
            int: the next number of the prime list
        Returns:
            gen_primes (list): list of prime numbers
    """
    a = 2
    gen_primes = []
    while True:
        if a is in eratosthenes(a+1):
            gen_primes.append(a)
            yield a
            a += 1
        else:
            a += 1
    return gen_primes


if __name__ == "__main__":
    import sys
    #makes sure a number is input
    if len(sys.argv) == 2:
        print(eratosthenes(int(sys.argv[1])))
    else:
        print("Error, needs 1 command line argument")
        exit(1)