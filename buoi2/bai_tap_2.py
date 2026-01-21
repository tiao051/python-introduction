def merge_arrays_with_sum():
    n = int(input("Nhập số phần tử của mảng a: "))
    m = int(input("Nhập số phần tử của mảng b: "))
    

    a = []
    for i in range(n):
        element = int(input(f"Nhập phần tử thứ {i + 1} của mảng a: "))
        a.append(element)
    
    
    b = []
    for i in range(m):
        element = int(input(f"Nhập phần tử thứ {i + 1} của mảng b: "))
        b.append(element)
    
    result = []
    min_len = min(len(a), len(b))
    
    for i in range(min_len):
        result.append(a[i] + b[i])
    
    if len(a) > min_len:
        result.extend(a[min_len:])
    else:
        result.extend(b[min_len:])
    
    print(f"Mảng a: {a}")
    print(f"Mảng b: {b}")
    print(f"Mảng kết quả: {result}")
    
    return result

merge_arrays_with_sum()

