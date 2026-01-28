class Rectangle:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length
    
    @property
    def width(self):
        return self._width

    def area(self):
        return self.length * self.width
    
    def display(self):
        print(f"Chiều dài: {self.length}")
        print(f"Chiều rộng: {self.width}")
        print(f"Diện tích: {self.area()}")

length = float(input("Nhập chiều dài hình chữ nhật: "))
width = float(input("Nhập chiều rộng hình chữ nhật: "))

rect = Rectangle(length, width)

rect.display()

print("\nThoát chương trình.")