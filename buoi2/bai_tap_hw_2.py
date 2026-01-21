


def create_new_list_from_two_lists():
    n = int(input("Nhập số phần tử của danh sách 1: "))
    list1 = []
    for i in range(n):
        element = int(input(f"Nhập phần tử thứ {i + 1} của danh sách 1: "))
        list1.append(element)
    
    m = int(input("Nhập số phần tử của danh sách 2: "))
    list2 = []
    for i in range(m):
        element = int(input(f"Nhập phần tử thứ {i + 1} của danh sách 2: "))
        list2.append(element)
    
    
    
    result = []
    
    
    for element in list1:
        if element % 2 != 0:
            result.append(element)
    
    
    for element in list2:
        if element % 2 == 0:
            result.append(element)
    
    print(f"Danh sách 1: {list1}")
    print(f"Danh sách 2: {list2}")
    print(f"Danh sách kết quả: {result}")
    
    return result

create_new_list_from_two_lists()

