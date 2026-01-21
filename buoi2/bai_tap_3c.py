

def print_column(a):
    k = int(input("Nhập số cột cần xuất (từ 1): "))
    k = k - 1  
    
    if 0 <= k < len(a[0]):
        column = [a[i][k] for i in range(len(a))]
        print(f"Các phần tử thuộc cột {k + 1}: {column}")
    else:
        print("Cột không tồn tại!")


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

print_column(a)

