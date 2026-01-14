data = input("Nhập dữ liệu (Họ tên, năm sinh, điểm, online): ")
parts = data.split(", ")

name = parts[0]
birth_year = int(parts[1])
score = float(parts[2])
online = parts[3] == "True"

print(f"Họ tên: {name}")
print(f"Năm sinh: {birth_year}")
print(f"Điểm: {score}")
print(f"Online: {online}")