while True:
    try:
        year = int(input("Nhập năm sinh: "))
        if 1900 <= year <= 2025:
            print(f"Năm sinh hợp lệ: {year}")
            break
        else:
            print("Năm sinh phải nằm trong khoảng 1900-2025!")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")
