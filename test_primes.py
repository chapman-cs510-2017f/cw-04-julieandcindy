#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Name: Julie Gardner-Hoag, Cynthia Parks
# Student ID: 2299636, 2303535
# Email: gardnerh@chapman.edu, cparks@chapman.edu
# Course: CS510 Fall 2017
# Assignment: Classwork 4
###

import primes

def test_primes():
    result=primes.eratosthenes(5)
    correct= [2, 3]
    assert result==correct
    
def test_primes2():
    result=primes.eratosthenes(50)
    correct = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert result==correct