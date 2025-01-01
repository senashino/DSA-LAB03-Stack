def evaluate_postfix(expression):

    stack = []

    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
            stack.append(result)

    return stack.pop()

expression = input("กรุณากรอกนิพจน์ Postfix : ")

result = evaluate_postfix(expression)

print(f"ผลลัพธ์ของนิพจน์ Postfix '{expression}' คือ: {result}")