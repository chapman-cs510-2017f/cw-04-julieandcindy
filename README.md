# CS510 CW 4

Julie Gardner-Hoag, Cynthia Parks

Student ID: 2299636, 2303535

Email: gardnerh@chapman.edu, cparks@chapman.edu

Course: CS510 Fall 2017

[![Build Status](https://travis-ci.org/chapman-cs510-2017f/cw-04-julieandcindy.svg?branch=master)](https://travis-ci.org/chapman-cs510-2017f/cw-04-julieandcindy)

## Specification

Complete the following exercises, saving your solutions in the indicated files. Write test functions in separate files with the naming format `test_MODULENAME.py`: GitHub will automatically run test functions starting with `test_` in these files with ```nosetests``` on every commit, indicating any failures via the Travis framework in the build status image above.

1. With your group, work through the [IPython and Jupyter slides](http://slides.com/profdressel/jupyter-overview) carefully, to make sure everything is now familiar. Be sure to use ```ipython3``` in a terminal to test code. Discuss amongst yourselves anything that is new or unclear.
1. Have one group member create a new Jupyter notebook ```cw04-primes.ipynb``` and open it within CoCalc using the click-interface. Go through the Jupyter tutorial in the Help menu, and examine the key shortcuts. Note that the keys follow vim conventions. Use the template notebook in the info repository as a guide for how to format your notebook properly as a group. You will use notebooks to present your results for this class in a neat, clear, and professional way. Be sure to switch the default kernel to Python 3 instead of the default Python 2 used by CoCalc.
1. Create a new python module ```primes.py```. Be sure to use ```#!/usr/bin/env python3``` at the top to force use of Python 3. Inside this module create a function ```eratosthenes(n)```. This function will take a positive integer ```n``` and return all prime numbers smaller than ```n```. You should use the Sieve of Eratosthenes algorithm for computing these primes, which works as follows: First generate all positive integers less than ```n```, starting from the number 2. Then remove all multiples of 2. Then remove all multiples of the next largest remaining (prime) number. Then repeat the last step until you reach the largest remaining number. Finally, return the set of remaining (prime) numbers. Think carefully about which (basic) python data structure you want to use to implement this algorithm before you start coding. (Recall: Basic data structures are list, dict, set, and tuple.)
1. Write a ```__main__``` section to make your ```primes.py``` python module executable as a script from the command line.
1. In the test file ```test_primes.py```, write a test function ```test_primes()``` that checks the output of ```eratosthenes(n)``` to ensure that it is correct. 
1. In your notebook, import the ```primes``` module at the top, and add a new section called "The Sieve of Eratosthenes". In this section, describe what the goal of the algorithm is, and how it works, in your own words. Describe your design decisions. Which data structure(s) did you use and why? Use $\LaTeX$ code as needed to format any math you write in a pretty way within the notebook. Finally, create code cells in the section that demonstrates the correct execution of your code.
1. In your primes module, create a new function ```gen_eratosthenes()``` that creates a generator for all the prime numbers. Rather than generating a fixed number of primes as in the previous implementation, such a generator must produce one new prime per iteration. Modify the algorithm to make this possible. 
1. In your notebook, add a new section called "Generating Prime Numbers" that describes and demonstrates your new generator. Explain your design decisions, and what is different compared to the previous implementation. Comment on whether your modification makes the original algorithm more efficient or not.
1. In your notebook, add a new section called "Benchmarking Implementations". In this section, use the ```%time``` and ```%timeit``` magic commands to compare the efficiency of your implementations. Which is faster? By how much? Does it match your prediction about efficiency above? Speculate about what is being slow about the slower implementation.
1. After your notebook is complete, spell-checked, and formatted properly, add and commit it to GitHub. Note that managing conflicts with Jupyter notebooks can be a pain, so I recommend having one person from your group be the official notebook editor, and having others in your group write code for the python modules in parallel.


## Assessment

This assignment was fun! Cindy enjoyed working with prime numbers. It was helpful to receive help on the "__main__"
part of the code. We now have a good example of how this works and how to exit with an exit code and print what error occurs. We both didn't have experience with Jupyter so it was interesting learning how to use it.

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

Julie Gardner-Hoag, Cynthia Parks
