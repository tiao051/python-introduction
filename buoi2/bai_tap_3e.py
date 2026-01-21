

def find_column_with_min_product(a):
    m = len(a)
    n = len(a[0])
    
    min_product = float('inf')
    min_col = -1
    
    for j in range(n):
        product = 1
        for i in range(m):
            product *= a[i][j]
        
        if product < min_product:
            min_product = product
            min_col = j
    
    column = [a[i][min_col] for i in range(m)]
    print(f"Cột {min_col + 1} có tích nhỏ nhất: {min_product}")
    print(f"Các phần tử: {column}")
    
    return min_col, min_product


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

find_column_with_min_product(a)

