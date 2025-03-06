# Write a Python program that inputs a list of words, separated by white
# space, and outputs how many times each word appears in the list. You
#  need not worry about efficiency at this point, however, as this topic is
#  something that will be addressed later in this book.

def count_times(data):
    dic = {}
    for word in data:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1

    for word, times in dic.items():
        print(f"The word '{word}' appears {times} times in the list")
