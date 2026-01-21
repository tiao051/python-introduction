

def print_row(a):
    k = int(input("Nhập số dòng cần xuất (từ 1): "))
    k = k - 1  
    
    if 0 <= k < len(a):
        print(f"Các phần tử thuộc dòng {k + 1}: {a[k]}")
    else:
        print("Dòng không tồn tại!")


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

print_row(a)

