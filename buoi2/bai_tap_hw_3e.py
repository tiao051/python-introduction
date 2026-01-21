


def check_symmetric_matrix(a):
    n = len(a)
    
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                print("Ma trận không đối xứng")
                return False
    
    print("Ma trận đối xứng")
    return True


n = int(input("Nhập cấp của ma trận: "))

a = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

check_symmetric_matrix(a)

