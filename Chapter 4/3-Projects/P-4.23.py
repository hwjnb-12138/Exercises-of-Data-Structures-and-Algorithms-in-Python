# Implement a recursive function with signature find(path, filename) that
#  reports all entries of the file system rooted at the given path having the
#  given file name.
import os


def find(path, filename):
    res = []
    for file in os.listdir(path):
        fullpath = os.path.join(path, file)
        if file == filename:
            res.append(fullpath)

        if os.path.isdir(fullpath):
            res.extend(find(fullpath, filename))
    return res
