def create_array_and_even_elements():
    n = int(input("Nhập số phần tử của mảng: "))
    
    a = []
    for i in range(n):
        element = int(input(f"Nhập phần tử thứ {i + 1}: "))
        a.append(element)
    
    b = [x for x in a if x % 2 == 0]
    
    print(f"Mảng a: {a}")
    print(f"Mảng b (các phần tử chẵn): {b}")
    
    return a, b

create_array_and_even_elements()

