# Checkoff-3
Topic: Python Libraries Implemented in C
For my checkoff i decided to investigate ways of using C inside of Python, and see which libraries implement the language.
I found that the main methods for using C in python are ctypes and Cython, and wrote some code snippets that take advantage of each

How to run code:
There are 3 experiments that I made. Run everything in the Linux terminal with python3 filename.py
- CDLL_test
    - this was a basic experiment to understand CDLL at a basic level.
    - Run python_program.py

- performance_test
    - this was a slightly less basic experiment where i used a long for loop and timers to check the running speed of python compared to the same code running in C and deffered to with CDLL
    - Run performance.py
      
- cython_test
    - this was my final experiment, where i did the same things as CDLL_test and performance_test, but used Cython logic instead.
    - I have confidence that the other experiments should run easily, but I'm not sure how well this one will run on a second machine.
    - I had to run 'apt install cython3' to get cython on my computer while i was coding. This may be necessary on another computer?
    - Run cython_test_2.py
    - cython_test.py also exists. I abandonded it because some things were ambiguous to me, but I think it may still be worth observing, as it shows how some Cython features can be implemented in Python language instead of Cython languages

Discoveries:
- Cython is bafflingly fast. I wrote a performance check that compared Python to C by counting to 100000 in each. when i used ctypes to count to 100k, it did it around 60x faster than python on average,
but when I used cython, it got it done over 1000x faster. Times were in 4 digit nanoseconds. I hope i didn't implement anything incorectly, because this difference is astonishing to me if it's the case.

- VSCode seems to have trouble recognizing Cython libraries. even when the library is fully functional, the code flags it as unknown

- There are even more ways of using C in python that I don't fully understand. Pygame uses SDL for example, but I didn't fully dive into how that works

- Shared library files exist. I wasn't aware of these prior, but they are a distinct type of file from an executable, and must be compiled differently

- .encode() is a function you can put at the end of a python string that makes it get passed in directly as bytes. This helped with ctypes because when I tried to use a python string for printf directly,
  it would only read the first character, but doing printf("".encode()) successfully read everything
