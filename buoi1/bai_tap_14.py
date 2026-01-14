seconds = int(input("Nhập số giây: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60
print(f"{hours} giờ {minutes} phút {secs} giây")
