#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Julie Gardner-Hoag, Cynthia Parks
# Student ID: 2299636, 2303535
# Email: gardnerh@chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 4
###

def eratosthenes(n):
    primes = []
    
    count = 2
    while count<=n-1:
        primes.append(count)
        count +=1
        
    p = 2
    
    while p<=n:
        for i in range(2, n+1):
            if i*p <= n:
                if i*p not in primes:
                    continue
                else:
                    primes.remove(i*p)
        p +=1
    
    return primes


        