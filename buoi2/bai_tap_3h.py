

def average_border_elements(a):
    m = len(a)
    n = len(a[0])
    
    border_elements = []
    
    
    border_elements.extend(a[0])
    
    
    if m > 1:
        border_elements.extend(a[m - 1])
    
    
    for i in range(1, m - 1):
        if n > 1:
            border_elements.append(a[i][0])
            border_elements.append(a[i][n - 1])
    
    if len(border_elements) > 0:
        avg = sum(border_elements) / len(border_elements)
        print(f"Các phần tử biên: {border_elements}")
        print(f"Trung bình cộng: {avg}")
    else:
        print("Không có phần tử biên!")


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

average_border_elements(a)

