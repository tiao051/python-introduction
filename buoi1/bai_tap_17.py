a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
operation = input("Nhập phép toán (+, -, *, /, //, %, **): ")

try:
    if operation == '+':
        result = a + b
    elif operation == '-':
        result = a - b
    elif operation == '*':
        result = a * b
    elif operation == '/':
        if b == 0:
            print("Lỗi: Không thể chia cho 0")
        else:
            result = a / b
    elif operation == '//':
        if b == 0:
            print("Lỗi: Không thể chia cho 0")
        else:
            result = a // b
    elif operation == '%':
        if b == 0:
            print("Lỗi: Không thể chia cho 0")
        else:
            result = a % b
    elif operation == '**':
        result = a ** b
    else:
        print("Phép toán không hợp lệ")
        result = None
    
    if result is not None:
        print(f"{a} {operation} {b} = {result}")
except Exception as e:
    print(f"Lỗi: {e}")
