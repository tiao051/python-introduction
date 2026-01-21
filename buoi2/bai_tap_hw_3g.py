


def print_lower_triangle_secondary_diagonal(a):
    n = len(a)
    
    print("Các phần tử thuộc tam giác dưới của đường chéo phụ (kể cả đường chéo phụ):")
    for i in range(n):
        for j in range(n):
            
            
            if i + j >= n - 1:
                print(f"a[{i}][{j}] = {a[i][j]}")


n = int(input("Nhập cấp của ma trận: "))

a = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

print_lower_triangle_secondary_diagonal(a)

