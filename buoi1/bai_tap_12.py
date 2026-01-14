base_salary = float(input("Nhập lương chính: "))
allowance = float(input("Nhập phụ cấp: "))
days_worked = float(input("Nhập số ngày đi làm: "))
total_salary = (base_salary + allowance) * days_worked / 26
print(f"Tổng lương nhận được: {total_salary}")
