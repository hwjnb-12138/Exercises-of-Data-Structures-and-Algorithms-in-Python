# In the Towers of Hanoi puzzle, we are given a platform with three pegs, a,
#  b,and c, sticking out of it. On peg a is a stack of n disks, each larger than
#  the next, so that the smallest is on the top and the largest is on the bottom.
#  The puzzle is to move all the disks from peg a to peg c, moving one disk
#  at a time, so that we never place a larger disk on top of a smaller one.
#  See Figure 4.15 for an example of the case n = 4. Describe a recursive
#  algorithm for solving the Towers of Hanoi puzzle for arbitrary n. (
#  : Consider first the subproblem of moving all but the nth disk from peg a to
#  another peg using the third as “temporary storage.”)

# 递归思路：移动n个原盘到目标杆的过程：先将前n-1个原盘移动到辅助杆→再将第n个圆盘移动到目标杆→最后把前n-1个圆盘移动到目标杆
def hanoi_puzzle(n, source, auxiliary, target):
    if n > 0:
        hanoi_puzzle(n-1, source, target, auxiliary)
        print(f"移动盘子 {n} 从 {source} 到 {target}")
        hanoi_puzzle(n-1, auxiliary, source, target)
