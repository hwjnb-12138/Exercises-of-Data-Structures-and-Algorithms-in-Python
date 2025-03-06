# Write a Python program that repeatedly reads lines from standard input
#  until an EOFError is raised, and then outputs those lines in reverse order
#  (a user can indicate end of input by typing ctrl-D).

l = list()
while True:
    tmp = input()
    l.append(tmp)
    if EOFError:
        break

l.reverse()
for line in l:
    print(line)

# lines = []
# while True:
#     try:
#         single = input()
#         lines.append(single)
#     except EOFError:
#         break
#
# print('\n'.join(reversed(lines)))
