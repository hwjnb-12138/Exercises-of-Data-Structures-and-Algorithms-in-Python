# Write a program for solving summation puzzles by enumerating and testing
#  all possible configurations. Using your program, solve the three puzzles
#  given in Section 4.4.3.

# 回答来自DeepSeek：
def PuzzleSolve(k, S, U, puzzle_test):
    """
    通用谜题求解递归算法
    :param k: 需要添加的元素个数
    :param S: 当前序列（部分解）
    :param U: 可用元素集合
    :param puzzle_test: 谜题测试函数，接受完整序列 S 返回布尔值
    :return: 解序列（如果找到），否则 None
    """
    # 创建 U 的副本避免修改原始集合
    U = set(U)

    for e in list(U):  # 遍历可用元素（创建副本避免修改迭代中的集合）
        # 添加元素到序列
        S.append(e)
        U.remove(e)

        if k == 1:
            # 检查是否解决谜题
            if puzzle_test(S):
                return S.copy()  # 返回解序列的副本
        else:
            # 递归求解
            solution = PuzzleSolve(k - 1, S, U, puzzle_test)
            if solution is not None:
                return solution

        # 回溯：移除元素并放回集合
        S.pop()
        U.add(e)

    return None  # 未找到解


# 求和谜题具体实现
def solve_sum_puzzle(word1, word2, word3):
    """解决形如 word1 + word2 = word3 的求和谜题"""
    # 提取所有唯一字母
    all_letters = list(set(word1 + word2 + word3))
    n = len(all_letters)

    # 验证字母数量
    if n > 10:
        raise ValueError("字母数量不能超过10")

    # 创建字母到索引的映射
    letter_to_index = {letter: idx for idx, letter in enumerate(all_letters)}

    # 定义谜题测试函数
    def puzzle_test(assignment):
        """检查当前数字分配是否满足等式"""
        # 将字母映射转换为数字映射
        mapping = {all_letters[i]: assignment[i] for i in range(n)}

        # 检查首字母不能为0
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[word3[0]] == 0:
            return False

        # 将单词转换为数字
        def word_to_num(word):
            num = 0
            for char in word:
                num = num * 10 + mapping[char]
            return num

        num1 = word_to_num(word1)
        num2 = word_to_num(word2)
        num3 = word_to_num(word3)

        return num1 + num2 == num3

    # 初始参数
    k = n  # 需要分配的字母数量
    S = []  # 初始序列（空）
    U = set(range(10))  # 可用数字 0-9

    # 使用通用算法求解
    solution = PuzzleSolve(k, S, U, puzzle_test)

    if solution:
        # 创建字母到数字的映射
        mapping = {all_letters[i]: solution[i] for i in range(n)}

        # 计算数值结果
        def word_to_num(word):
            return int(''.join(str(mapping[c]) for c in word))

        num1 = word_to_num(word1)
        num2 = word_to_num(word2)
        num3 = word_to_num(word3)

        return {
            "mapping": mapping,
            "equation": f"{num1} + {num2} = {num3}",
            "result": (num1, num2, num3)
        }
    return None


# 测试求解
if __name__ == "__main__":
    # 测试用例
    puzzles = [
        ("pot", "pan", "bib"),  # 示例谜题
        ("dog", "cat", "pig"),  # 经典谜题
        ("boy", "girl", "baby"),  # 另一个示例
    ]

    for words in puzzles:
        print(f"\n求解谜题: {words[0]} + {words[1]} = {words[2]}")
        solution = solve_sum_puzzle(*words)

        if solution:
            print("找到解！")
            print("字母映射:")
            for letter, digit in solution["mapping"].items():
                print(f"  {letter} = {digit}")
            print("等式:", solution["equation"])
        else:
            print("未找到解")