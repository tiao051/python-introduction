

def print_even_row_odd_column(a):
    m = len(a)
    n = len(a[0])
    
    print("Các phần tử thuộc dòng chẵn (từ 1) và cột lẻ (từ 1):")
    for i in range(m):
        for j in range(n):
            
            if (i + 1) % 2 == 0 and (j + 1) % 2 == 1:  
                print(f"a[{i}][{j}] = {a[i][j]}")


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

print_even_row_odd_column(a)

