# Describe an algorithm for finding both the minimum and maximum of n
#  numbers using fewer than 3n/2 comparisons.

def find_min_max(arr):
    n = len(arr)
    # 处理空数组边界情况
    if n == 0:
        return (None, None)

    # 初始化最小值和最大值
    if n % 2 == 1:  # 奇数长度
        min_val = max_val = arr[0]
        start_index = 1
    else:  # 偶数长度
        if arr[0] < arr[1]:
            min_val, max_val = arr[0], arr[1]
        else:
            min_val, max_val = arr[1], arr[0]
        start_index = 2

        # 成对处理剩余元素
    for i in range(start_index, n, 2):
        a, b = arr[i], arr[i + 1]

        # 比较当前对中的大小关系（1次比较）
        if a < b:
            current_min, current_max = a, b
        else:
            current_min, current_max = b, a

            # 更新全局最小值（1次比较）
        if current_min < min_val:
            min_val = current_min

            # 更新全局最大值（1次比较）
        if current_max > max_val:
            max_val = current_max

    return (min_val, max_val)
