

def find_row_with_max_sum(a):
    max_sum = float('-inf')
    max_row = -1
    
    for i in range(len(a)):
        row_sum = sum(a[i])
        if row_sum > max_sum:
            max_sum = row_sum
            max_row = i
    
    print(f"Dòng {max_row + 1} có tổng lớn nhất: {max_sum}")
    print(f"Các phần tử: {a[max_row]}")
    
    return max_row, max_sum


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

find_row_with_max_sum(a)

