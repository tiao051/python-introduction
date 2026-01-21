

def convert_negative_to_absolute(a):
    m = len(a)
    n = len(a[0])
    
    for i in range(m):
        for j in range(n):
            if a[i][j] < 0:
                a[i][j] = abs(a[i][j])
    
    print("Mảng sau khi chuyển đổi:")
    for row in a:
        print(row)
    
    return a


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

convert_negative_to_absolute(a)

