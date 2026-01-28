class ListManager:
    def __init__(self):
        self._items = []
    
    @property
    def items(self):
        return self._items
    
    def add(self, value):
        self._items.append(value)
        print(f"Đã thêm '{value}' vào danh sách")
    
    def remove(self, value):
        if value in self._items:
            self._items.remove(value)
            print(f"Đã xóa '{value}' khỏi danh sách")
        else:
            print(f"Không tìm thấy '{value}' trong danh sách")
    
    def display(self):
        if not self._items:
            print("Danh sách trống")
        else:
            print("Danh sách hiện tại:", self._items)


def main():
    manager = ListManager()
    
    while True:
        print("\n=== QUẢN LÝ DANH SÁCH ===")
        print("1. Thêm phần tử")
        print("2. Xóa phần tử")
        print("3. Hiển thị danh sách")
        print("4. In danh sách cuối cùng và thoát")
        
        choice = input("Chọn chức năng (1-4): ")
        
        match choice:
            case "1":
                value = input("Nhập giá trị cần thêm: ")
                manager.add(value)
            case "2":
                value = input("Nhập giá trị cần xóa: ")
                manager.remove(value)
            case "3":
                manager.display()
            case "4":
                print("\n=== DANH SÁCH CUỐI CÙNG ===")
                manager.display()
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ, vui lòng thử lại")


if __name__ == "__main__":
    main()
