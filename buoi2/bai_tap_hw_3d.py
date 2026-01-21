

def check_all_even(a):
    m = len(a)
    n = len(a[0])
    
    for i in range(m):
        for j in range(n):
            if a[i][j] % 2 != 0:
                print("Mảng không toàn chẵn (có phần tử lẻ)")
                return False
    
    print("Mảng toàn chẵn")
    return True


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

check_all_even(a)

