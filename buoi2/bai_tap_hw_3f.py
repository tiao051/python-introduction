

def check_main_diagonal_increasing(a):
    n = len(a)
    
    for i in range(n - 1):
        if a[i][i] >= a[i + 1][i + 1]:
            print("Đường chéo chính không tăng dần")
            return False
    
    print("Đường chéo chính tăng dần")
    return True


n = int(input("Nhập cấp của ma trận: "))

a = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

check_main_diagonal_increasing(a)

