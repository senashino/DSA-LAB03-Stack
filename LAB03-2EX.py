#โปรแกรมแปลงเลขฐาน

def convert_to_binary(number):

    stack = []

    while number > 0:
        remainder = number % 2
        stack[len(stack):] = [str(remainder)]
        number = number // 2

    if len(stack) == 0:
        stack = ['0']

    reversed_binary = ''
    for i in range(len(stack) - 1, -1, -1):
        reversed_binary += stack[i]

    return reversed_binary

def convert_to_hexadecimal(number):
    # สร้าง stack เป็นลิสต์เปล่า
    stack = []
    hex_digits = '0123456789ABCDEF'

    while number > 0:
        remainder = number % 16
        stack[len(stack):] = [hex_digits[remainder]]
        number = number // 16

    if len(stack) == 0:
        stack = ['0']

    reversed_hex = ''
    for i in range(len(stack) - 1, -1, -1):
        reversed_hex += stack[i]

    return reversed_hex

number = int(input("กรุณากรอกเลขฐาน 10: "))

#แปลงเป็นฐาน 2
binary_result = convert_to_binary(number)

#แปลงเป็นฐาน 16
hexadecimal_result = convert_to_hexadecimal(number)

print(f"เลขฐาน 2: {binary_result}")
print(f"เลขฐาน 16: {hexadecimal_result}")
