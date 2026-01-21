

def average_product_non_border_elements(a):
    m = len(a)
    n = len(a[0])
    
    non_border_elements = []
    
    
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            non_border_elements.append(a[i][j])
    
    if len(non_border_elements) > 0:
        product = 1
        for element in non_border_elements:
            product *= element
        avg = product / len(non_border_elements)
        print(f"Các phần tử không thuộc biên: {non_border_elements}")
        print(f"Tích: {product}")
        print(f"Trung bình tích: {avg}")
    else:
        print("Không có phần tử không thuộc biên!")


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

average_product_non_border_elements(a)

