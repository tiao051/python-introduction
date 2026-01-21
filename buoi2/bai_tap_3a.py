

import random

def create_2d_array():
    m = int(input("Nhập số dòng: "))
    n = int(input("Nhập số cột: "))
    
    a = []
    for i in range(m):
        row = []
        for j in range(n):
            element = random.randint(1, 100)
            row.append(element)
        a.append(row)
    
    print("Mảng 2 chiều:")
    for row in a:
        print(row)
    
    return a

create_2d_array()

