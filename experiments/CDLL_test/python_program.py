import ctypes
import os


print("This is a python program doing python things")

#this gets the current working directory of the file
c_filepath = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "c_program.so")

c_file = ctypes.CDLL(c_filepath)
c_file.test_message()

#we have to use .encode() to send the bytes of the string,
#because it will only print the first character if we send in
#a python string directly
c_file.printf("You can even use functions that aren't directly defined! Radical!\n".encode())

