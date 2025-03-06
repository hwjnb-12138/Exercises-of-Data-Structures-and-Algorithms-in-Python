# Write a Python program that can take a positive integer greater than 2 as
#  input and write out the number of times one must repeatedly divide this
#  number by 2 before getting a value less than 2.

def divide(n, times=0):
    if n < 2:
        print(times)
    else:
        times += 1
        divide(n / 2, times)
