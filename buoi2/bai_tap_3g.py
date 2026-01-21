

def average_even_elements_in_odd_rows(a):
    m = len(a)
    even_elements = []
    
    for i in range(m):
        if (i + 1) % 2 == 1:  
            for j in range(len(a[i])):
                if a[i][j] % 2 == 0:  
                    even_elements.append(a[i][j])
    
    if len(even_elements) > 0:
        avg = sum(even_elements) / len(even_elements)
        print(f"Các phần tử chẵn trong dòng lẻ: {even_elements}")
        print(f"Trung bình cộng: {avg}")
    else:
        print("Không có phần tử chẵn trong dòng lẻ!")


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))

a = []
for i in range(m):
    row = []
    for j in range(n):
        element = int(input(f"Nhập a[{i}][{j}]: "))
        row.append(element)
    a.append(row)

average_even_elements_in_odd_rows(a)

