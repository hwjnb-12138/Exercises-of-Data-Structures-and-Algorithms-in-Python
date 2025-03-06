# Write a Python program that simulates a handheld calculator. Your pro-
# gram should process input from the Python console representing buttons
#  that are “pushed,” and then output the contents of the screen after each op-
# eration is performed. Minimally, your calculator should be able to process
#  the basic arithmetic operations and a reset/clear operation.

class Calculator:
    def __init__(self):
        self.reset()

    def reset(self):
        """重置所有计算器状态"""
        self.screen = "0"  # 当前显示内容
        self.buffer = ""  # 输入缓冲区
        self.operator = None  # 当前运算符
        self.stored_value = 0  # 存储的数值
        self.new_number = True  # 是否开始新数字输入

    def process_input(self, button):
        """处理单个按钮输入"""
        button = button.upper()

        if button == "Q":  # 退出程序
            return False
        elif button == "C":  # 清除重置
            self.reset()
        elif button in "0123456789":
            self._handle_digit(button)
        elif button == ".":
            self._handle_decimal()
        elif button in "+-*/":
            self._handle_operator(button)
        elif button == "=":
            self._handle_equals()

        return True

    def _handle_digit(self, digit):
        """处理数字输入"""
        if self.new_number:
            self.buffer = digit
            self.new_number = False
        else:
            self.buffer += digit
        self.screen = self.buffer

    def _handle_decimal(self):
        """处理小数点"""
        if "." not in self.buffer:
            if not self.buffer:
                self.buffer = "0"
            self.buffer += "."
            self.screen = self.buffer
            self.new_number = False

    def _handle_operator(self, op):
        """处理运算符"""
        if self.buffer:
            self._perform_calculation()
        self.operator = op
        self.stored_value = float(self.screen)
        self.new_number = True

    def _handle_equals(self):
        """处理等号"""
        if self.operator and not self.new_number:
            self._perform_calculation()
            self.operator = None

    def _perform_calculation(self):
        """执行实际计算"""
        try:
            current = float(self.buffer) if self.buffer else float(self.screen)
            if self.operator == "+":
                result = self.stored_value + current
            elif self.operator == "-":
                result = self.stored_value - current
            elif self.operator == "*":
                result = self.stored_value * current
            elif self.operator == "/":
                result = self.stored_value / current
            else:
                result = current

            self.screen = str(result).rstrip("0").rstrip(".") if "." in str(result) else str(result)
            self.stored_value = result
            self.buffer = ""
        except ZeroDivisionError:
            self.screen = "Error"
            self.reset()


if __name__ == "__main__":
    calc = Calculator()
    print("手持计算器模拟器（输入Q退出，C清除）")
    while True:
        print(f"\n当前屏幕: {calc.screen}")
        btn = input("输入按钮: ").strip()
        if not calc.process_input(btn):
            break
