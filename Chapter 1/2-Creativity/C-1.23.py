#  Give an example of a Python code fragment that attempts to write an ele-
# ment to a list based on an index that may be out of bounds. If that index
#  is out of bounds, the program should catch the exception that results, and
#  print the following error message:
#  “Don’t try buffer overflow attacks in Python!”

l = list()
def write_element(i, data):
    try:
        l[i] = data
    except IndexError:
        print("Don’t try buffer overflow attacks in Python!")
