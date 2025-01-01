#โปรแกรมกลับลำดับตัวอักษร

text = input("กรุณากรอกข้อความ : ")

stack = []

for i in range(len(text)):
    stack.append(text[i])

reversed_text = ""

for i in range(len(stack)):
    reversed_text += stack[len(stack) - 1 - i]

print("ข้อความที่กลับลำดับแล้ว:", reversed_text)