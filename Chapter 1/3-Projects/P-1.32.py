# Write a Python program that can simulate a simple calculator, using the
#  console as the exclusive input and output device. That is, each input to the
#  calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
#  can be done on a separate line. After each such input, you should output
#  to the Python console what would be displayed on your calculator.

# This result comes from DeepSeek
current_value = 0.0
first_operand = None
pending_operator = None

while True:
    line = input().strip()
    if not line:
        continue

    # Check if the input is a number
    try:
        num = float(line)
        current_value = num
        print(current_value)
        continue
    except ValueError:
        pass

    # Process operators or '='
    if line in ['+', '-', '*', '/', '=']:
        if line == '=':
            if pending_operator is not None and first_operand is not None:
                try:
                    if pending_operator == '+':
                        result = first_operand + current_value
                    elif pending_operator == '-':
                        result = first_operand - current_value
                    elif pending_operator == '*':
                        result = first_operand * current_value
                    elif pending_operator == '/':
                        if current_value == 0:
                            raise ZeroDivisionError
                        result = first_operand / current_value
                    current_value = result
                    print(current_value)
                except ZeroDivisionError:
                    print("Error")
                    current_value = 0.0
                    first_operand = None
                    pending_operator = None
                # Reset after processing '='
                first_operand = None
                pending_operator = None
            else:
                # No pending operation, display current value
                print(current_value)
        else:
            # Handle other operators: '+', '-', '*', '/'
            had_pending = pending_operator is not None
            if had_pending:
                try:
                    if pending_operator == '+':
                        result = first_operand + current_value
                    elif pending_operator == '-':
                        result = first_operand - current_value
                    elif pending_operator == '*':
                        result = first_operand * current_value
                    elif pending_operator == '/':
                        if current_value == 0:
                            raise ZeroDivisionError
                        result = first_operand / current_value
                    current_value = result
                    print(current_value)
                except ZeroDivisionError:
                    print("Error")
                    current_value = 0.0
                    first_operand = None
                    pending_operator = None
                    # Skip further processing for this input
                    continue
            # Update first_operand and pending_operator after processing
            first_operand = current_value
            pending_operator = line
            # Print if there was no pending operator before
            if not had_pending:
                print(current_value)
    else:
        # Ignore invalid inputs as per problem statement
        pass
