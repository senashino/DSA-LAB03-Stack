class Stack:
    def __init__(self):
        """สร้าง Stack เปล่า"""
        self.items = []     # ใช้ list เก็บข้อมูลใน Stack
    
    def is_empty(self):
        """ตรวจสอบว่า Stack ว่างหรือไม่"""
        return len(self.items) == 0
    
    def push(self, item):
        """เพิ่มข้อมูลเข้า Stack"""
        self.items.append(item)
    
    def pop(self):
        """นำข้อมูลออกจาก Stack"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
    
    def peek(self):
        """ดูข้อมูลที่อยู่บนสุดของ Stack"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
    
    def size(self):
        """ดูขนาดของ Stack"""
        return len(self.items)

# ทดสอบการใช้งานของ Stack class
if __name__ == "__main__":
    # สร้าง Stack
    stack = Stack()
    print("1. ทดสอบการ push ข้อมูล:")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print("Stack หลังจากการ push 5 ตัว:", stack.items)

    print("ข้อมูลบนสุดของ Stack (peek):", stack.peek())

    print("ข้อมูลที่ถูก pop ออก 3 ตัว:", stack.pop(), stack.pop(), stack.pop())

    print("Stack หลังจากการ pop 3 ตัว:", stack.items)

    print("ขนาดของ Stack:", stack.size())