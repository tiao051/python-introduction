import math

class Triangle:
    def __init__(self):
        self._a = 0.0
        self._b = 0.0
        self._c = 0.0
    
    @property
    def a(self):
        return self._a
    
    @property
    def b(self):
        return self._b
    
    @property
    def c(self):
        return self._c
    
    def _is_valid_triangle(self, a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Không phải tam giác hợp lệ. Tổng 2 cạnh phải lớn hơn cạnh thứ 3")
        return True
    
    def inputSides(self):
        while True:
            try:
                a = float(input("Nhập cạnh a: "))
                b = float(input("Nhập cạnh b: "))
                c = float(input("Nhập cạnh c: "))
                
                if a <= 0 or b <= 0 or c <= 0:
                    raise ValueError("Các cạnh phải lớn hơn 0")
                
                self._is_valid_triangle(a, b, c)
                self._a = a
                self._b = b
                self._c = c
                break
            except ValueError as e:
                print(f"Lỗi: {e}")
    
    def getTriangleType(self):
        if self.a == self.b == self.c:
            return "Tam giác đều"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Tam giác cân"
        else:
            a_sq = self.a ** 2
            b_sq = self.b ** 2
            c_sq = self.c ** 2
            
            if (abs(a_sq + b_sq - c_sq) < 1e-9 or 
                abs(a_sq + c_sq - b_sq) < 1e-9 or 
                abs(b_sq + c_sq - a_sq) < 1e-9):
                return "Tam giác vuông"
            else:
                return "Tam giác thường"
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.perimeter() / 2
        area_squared = s * (s - self.a) * (s - self.b) * (s - self.c)
        
        if area_squared < 0:
            return 0
        
        return math.sqrt(area_squared)
    
    def displayInfo(self):
        print(f"Cạnh a: {self.a}")
        print(f"Cạnh b: {self.b}")
        print(f"Cạnh c: {self.c}")
        print(f"Loại tam giác: {self.getTriangleType()}")
        print(f"Chu vi: {self.perimeter():.2f}")
        print(f"Diện tích: {self.area():.2f}")

triangle = Triangle()

triangle.inputSides()
print()
triangle.displayInfo()

print("\nThoát chương trình.")
