def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_operator(operand2, operand1, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

def evaluate_infix(expression):
    values = []
    operators = []

    i = 0
    while i < len(expression):
        char = expression[i]

        if char == ' ':
            i += 1
            continue

        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
            continue

        elif char == '(':
            operators.append(char)

        elif char == ')':
            while operators and operators[-1] != '(':
                operator = operators.pop()
                operand2 = values.pop()
                operand1 = values.pop()
                values.append(apply_operator(operand2, operand1, operator))
            operators.pop()

        elif char in '+-*/':
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(char)):
                operator = operators.pop()
                operand2 = values.pop()
                operand1 = values.pop()
                values.append(apply_operator(operand2, operand1, operator))
            operators.append(char)

        i += 1

    while operators:
        operator = operators.pop()
        operand2 = values.pop()
        operand1 = values.pop()
        values.append(apply_operator(operand2, operand1, operator))

    return values[-1]

expression = input("กรุณากรอกนิพจน์ Infix : ")

result = evaluate_infix(expression)

print(f"ผลลัพธ์ของนิพจน์ Infix '{expression}' คือ : {result}")
