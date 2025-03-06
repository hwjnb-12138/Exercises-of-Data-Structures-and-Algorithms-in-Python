# A common punishment for school children is to write out a sentence mul-
# tiple times. Write a Python stand-alone program that will write out the
#  following sentence one hundred times: “I will never spam my friends
#  again.” Your program should number each of the sentences and it should
#  make eight different random-looking typos.

import random

sample = random.sample(range(100), 8)
l = ["I will never spam my friends again." for _ in range(100)]

for i in sample:
    Num = random.randint(0, 34)
    Rep = random.randint(97, 122)
    if l[i][Num] != " " and l[i][Num] != ".":
        temp = list(l[i])
        temp[Num] = chr(Rep)
        l[i] = ''.join(temp)

for i in range(100):
    print(str(i + 1) + ". " +l[i])


# # The result comes from DeepSeek
# def generate_typo(s):
#     """生成随机的拼写错误（仅限字母替换、删除、插入和调换）"""
#     chars = list(s)
#     letter_indices = [i for i, c in enumerate(chars) if c.isalpha()]
#     if not letter_indices:
#         return s
#
#     index = random.choice(letter_indices)
#     original_char = chars[index]
#     typo_type = random.choice(['replace', 'delete', 'insert', 'swap'])
#
#     try:
#         if typo_type == 'replace':
#             new_char = random.choice('abcdefghijklmnopqrstuvwxyz')
#             if original_char.isupper():
#                 new_char = new_char.upper()
#             chars[index] = new_char
#
#         elif typo_type == 'delete':
#             del chars[index]
#
#         elif typo_type == 'insert':
#             new_char = random.choice('abcdefghijklmnopqrstuvwxyz')
#             if index > 0 and chars[index - 1].isupper():
#                 new_char = new_char.upper()
#             chars.insert(index, new_char)
#
#         elif typo_type == 'swap' and index < len(chars) - 1:
#             chars[index], chars[index + 1] = chars[index + 1], chars[index]
#
#     except IndexError:
#         pass
#
#     return ''.join(chars)
#
#
# # 生成8种不重复的错误句子
# base_sentence = "I will never spam my friends again."
# unique_typos = set()
#
# while len(unique_typos) < 8:
#     modified = generate_typo(base_sentence)
#     if modified != base_sentence:
#         unique_typos.add(modified)
#
#     # 构建最终输出列表并打乱顺序
# sentences = [base_sentence] * 92 + list(unique_typos)
# random.shuffle(sentences)
#
# # 格式化输出
# for idx, text in enumerate(sentences, 1):
#     print(f"{idx}. {text}")
