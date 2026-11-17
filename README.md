# Checkoff-3
Topic: Python Libraries Implemented in C
For my checkoff i decided to investigate ways of using C inside of Python, and see which libraries implement the language.
I found that the main methods for using C in python are ctypes and Cython, and wrote some code snippets that take advantage of each

Discoveries:
Cython is bafflingly fast. I wrote a performance check that compared Python to C by counting to 100000 in each. when i used ctypes to count to 100k, it did it around 60x faster than python on average,
but when I used cython, it got it done over 1000x faster. Times were in 4 digit nanoseconds. I hope i didn't implement anything incorectly, because this difference is astonishing to me if it's the case.
