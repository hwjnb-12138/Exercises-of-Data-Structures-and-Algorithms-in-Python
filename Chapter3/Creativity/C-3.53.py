# An evil king has n bottles of wine, and a spy has just poisoned one of
#  them. Unfortunately, they do not know which one it is. The poison is very
#  deadly; just one drop diluted even a billion to one will still kill. Even so,
#  it takes a full month for the poison to take effect. Design a scheme for
#  determining exactly which one of the wine bottles was poisoned in just
#  one month’s time while expending O(logn) taste testers.

# 每位品尝者代表一个二进制位，第i个品尝者将会喝所有第i位为1的酒，例如：
# 第i位品尝者     喝的酒
#   1        1，3，5，7（xx1）
#   2        2，3，6，7（x1x）
#   3        4，5，6，7（1xx）
# 一个月后，哪位品尝者中毒，则其对应的二进制位为1，组合二进制位就可以得出毒酒的编号
# 例如，若第1、3位中毒，第2位正常，则毒酒编号为101，即第5瓶
