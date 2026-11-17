import goku
import time

print(goku.say_something())
print("\n\n")
start_time = time.time_ns();
a = 0
for i in range(100000):
    a += 1

end_time = time.time_ns();
elapsed_time = end_time - start_time
print("Counting to 100,000 in Python: " + str(elapsed_time) + " nanoseconds\n")



start_time = time.time_ns();
b = goku.goku_count()
print("Goku finished counting! b = " + str(b))
end_time = time.time_ns();
c_elapsed_time = end_time - start_time
print("Counting to 100,000 in C: " + str(c_elapsed_time) + " nanoseconds\n")
print("Goku is " + str(elapsed_time/c_elapsed_time) + " times faster\n\n")