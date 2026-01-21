

def check_secondary_diagonal_decreasing(a):
    n = len(a)
    
    
    diagonal = [a[i][n - 1 - i] for i in range(n)]
    
    for i in range(n - 1):
        if diagonal[i] <= diagonal[i + 1]:
            print("Đường chéo phụ không giảm dần")
            return False
    
    print("Đường chéo phụ giảm dần")
    print(f"Đường chéo phụ: {diagonal}")
    return True


n = int(input("Nhập cấp của ma trận: "))

a = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

check_secondary_diagonal_decreasing(a)

