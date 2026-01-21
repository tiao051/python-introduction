


def sum_upper_triangle_secondary_diagonal(a):
    n = len(a)
    total = 0
    
    
    
    for i in range(n):
        for j in range(n):
            
            
            if i + j == n - 1 or i < n - 1 - i:
                total += a[i][j]
    
    print(f"Tổng: {total}")
    return total


n = int(input("Nhập cấp của ma trận: "))

a = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

sum_upper_triangle_secondary_diagonal(a)

