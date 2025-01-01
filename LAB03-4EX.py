#การตรวจสอบ JSON string

def is_valid_json(json_str):

    stack = []

    i = 0
    while i < len(json_str):
        char = json_str[i]

        if char == '{' or char == '[' or char == '"':
            stack.append(char)
        
        elif char == '}' or char == ']' or char == '"':
            if not stack:
                return False
            top = stack.pop()
            if char == '}' and top != '{':
                return False
            elif char == ']' and top != '[':
                return False
            elif char == '"' and top != '"':

                if i > 0 and json_str[i-1] != "\\":
                    return False

        i += 1

    return len(stack) == 0

json_string = input("กรุณากรอก JSON string: ")

if is_valid_json(json_string):
    print("JSON string ถูกต้อง")
else:
    print("JSON string ไม่ถูกต้อง")
