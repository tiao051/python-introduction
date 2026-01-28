class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self._real = real
        self._imag = imag
    
    @property
    def real(self):
        return self._real
    
    @property
    def imag(self):
        return self._imag
    
    @real.setter
    def real(self, value):
        self._real = value
    
    @imag.setter
    def imag(self, value):
        self._imag = value

    def inputComplex(self):
        while True:
            try:
                real = float(input("Nhập phần thực: "))
                imag = float(input("Nhập phần ảo: "))
                self._real = real
                self._imag = imag
                break
            except ValueError:
                print("Lỗi: Vui lòng nhập số hợp lệ!")
    
    def displayComplex(self):
        if self._imag >= 0:
            print(f"{self._real} + {self._imag}i")
        else:
            print(f"{self._real} - {abs(self._imag)}i")
    
    def add(self, other):
        return ComplexNumber(self._real + other._real, self._imag + other._imag)
    
    def subtract(self, other):
        return ComplexNumber(self._real - other._real, self._imag - other._imag)
    
    def multiply(self, other):
        real_part = (self._real * other._real) - (self._imag * other._imag)
        imag_part = (self._real * other._imag) + (self._imag * other._real)
        return ComplexNumber(real_part, imag_part)
    
    def divide(self, other):
        denom = (other._real ** 2) + (other._imag ** 2)
        if denom == 0:
            raise ValueError("Không thể chia cho 0")
        
        real_part = ((self._real * other._real) + (self._imag * other._imag)) / denom
        imag_part = ((self._imag * other._real) - (self._real * other._imag)) / denom
        return ComplexNumber(real_part, imag_part)


def main():
    print("=== Chương trình tính toán số phức ===\n")
    
    z1 = ComplexNumber()
    print("Nhập số phức thứ nhất:")
    z1.inputComplex()
    
    z2 = ComplexNumber()
    print("\nNhập số phức thứ hai:")
    z2.inputComplex()
    
    print("\n=== Kết quả ===")
    
    print("\nSố phức thứ nhất: ", end="")
    z1.displayComplex()
    
    print("Số phức thứ hai: ", end="")
    z2.displayComplex()
    
    print("\nCộng: ", end="")
    z1.add(z2).displayComplex()
    
    print("Trừ: ", end="")
    z1.subtract(z2).displayComplex()
    
    print("Nhân: ", end="")
    z1.multiply(z2).displayComplex()
    
    try:
        print("Chia: ", end="")
        z1.divide(z2).displayComplex()
    except ValueError as e:
        print(f"Lỗi: {e}")


if __name__ == "__main__":
    main()
