# Write a short program that takes as input three integers, a, b,and c, from
#  the console and determines if they can be used in a correct arithmetic
#  formula (in the given order), like “a+b = c,” “a = b−c,” or “a∗b = c.”

# This result comes from DeepSeek
def check_arithmetic_formula():
    try:
        a = int(input("Enter integer a: "))
        b = int(input("Enter integer b: "))
        c = int(input("Enter integer c: "))
    except ValueError:
        print("Invalid input. Please enter integers.")
        return

        # 检查五种可能的算术公式
    valid = (
            (a + b == c) or
            (a - b == c) or
            (a * b == c) or
            (a / b == c if b != 0 else False) or  # 避免除零错误
            (b != 0 and a == c / b)  # 反向检查 a = c / b
    )

    print(f"Can form a valid formula: {valid}")


# 调用函数执行
check_arithmetic_formula()
