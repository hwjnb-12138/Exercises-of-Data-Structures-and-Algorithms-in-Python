# Write a short recursive Python function that takes a character string s and
#  outputs its reverse. For example, the reverse of pots&pans would be
#  snap&stop.

def reverse(s, start, end):
    s = list(s)
    if start >= end:
        return s

    s[start], s[end] = s[end], s[start]
    return ''.join(reverse(s, start+1, end-1))

# def reverse(s):
#     if len(s) <= 1:  # 基线条件：空串或单字符
#         return s
#     # 递归：首字符移到末尾 + 反转剩余部分
#     return reverse(s[1:]) + s[0]
