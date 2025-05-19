# Write a Python program that inputs a document and then outputs a barchart plot of the
# frequencies of each alphabet character that appears in that document.
import matplotlib.pyplot as plt

filename = input("Enter document path: ").strip()
dic = {}
with open(filename, 'r') as f:
    while True:
        char = f.read(1)

        if not char:
            break

        if char.isalpha():
            char = char.lower()
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

letters = sorted(dic.keys())
nums = [dic[k] for k in letters]
plt.bar(letters, nums)
plt.xlabel("Letters")
plt.ylabel("Frequency")
plt.show()
