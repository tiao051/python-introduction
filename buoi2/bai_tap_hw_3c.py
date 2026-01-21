

def replace_even_with_x(a, x):
    m = len(a)
    n = len(a[0])
    
    for i in range(m):
        for j in range(n):
            if a[i][j] % 2 == 0:
                a[i][j] = x
    
    print(f"Mảng sau khi thay thế các phần tử chẵn bằng {x}:")
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

x = int(input("Nhập giá trị x: "))
replace_even_with_x(a, x)

