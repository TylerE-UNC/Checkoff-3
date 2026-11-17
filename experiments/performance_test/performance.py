import time
import os
import ctypes


start_time = time.time_ns();
a = 0
for i in range(100000):
    a += 1

end_time = time.time_ns();
elapsed_time = end_time - start_time
print("Counting to 100,000 in Python: " + str(elapsed_time) + " nanoseconds\n")


c_filepath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "performance.so")

c_file = ctypes.CDLL(c_filepath)

start_time = time.time_ns();
c_file.counter()
end_time = time.time_ns();
c_elapsed_time = end_time - start_time
print("Counting to 100,000 in C: " + str(c_elapsed_time) + " nanoseconds\n")
print("C is " + str(elapsed_time/c_elapsed_time) + " times faster\n\n")