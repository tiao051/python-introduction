class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self._numerator = numerator
        self._denominator = denominator
    
    @property
    def numerator(self):
        return self._numerator
    
    @property
    def denominator(self):
        return self._denominator
    
    def _greatest_common_divisor(self, a, b):
        a, b = abs(a), abs(b)
        while b:
            a, b = b, a % b
        return a
    
    def _simplify_fraction(self, num, denom):
        if denom == 0:
            raise ValueError("Mẫu số không được bằng 0")
        
        divisor = self._greatest_common_divisor(num, denom)
        num //= divisor
        denom //= divisor
        
        if denom < 0:
            num = -num
            denom = -denom
        
        return num, denom
    
    def inputFraction(self):
        while True:
            try:
                num = int(input("Nhập tử số: "))
                denom = int(input("Nhập mẫu số: "))
                
                if denom == 0:
                    raise ValueError("Mẫu số không được bằng 0")
                
                self._numerator = num
                self._denominator = denom
                break
            except ValueError as e:
                print(f"Lỗi: {e}")
    
    def displayFraction(self):
        if self.denominator == 1:
            print(f"Phân số: {self.numerator}")
        else:
            print(f"Phân số: {self.numerator}/{self.denominator}")
    
    def simplify(self):
        num, denom = self._simplify_fraction(self.numerator, self.denominator)
        self._numerator = num
        self._denominator = denom
    
    def reciprocal(self):
        if self.numerator == 0:
            raise ValueError("Không thể lấy nghịch đảo của phân số có tử số bằng 0")
        
        num, denom = self._simplify_fraction(self.denominator, self.numerator)
        return Fraction(num, denom)
    
    def add(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_denom = self.denominator * other.denominator
        result = Fraction(new_num, new_denom)
        result.simplify()
        return result
    
    def subtract(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_denom = self.denominator * other.denominator
        result = Fraction(new_num, new_denom)
        result.simplify()
        return result
    
    def multiply(self, other):
        new_num = self.numerator * other.numerator
        new_denom = self.denominator * other.denominator
        result = Fraction(new_num, new_denom)
        result.simplify()
        return result
    
    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Không thể chia cho phân số có tử số bằng 0")
        
        new_num = self.numerator * other.denominator
        new_denom = self.denominator * other.numerator
        result = Fraction(new_num, new_denom)
        result.simplify()
        return result

frac1 = Fraction()
frac2 = Fraction()

print("Nhập phân số thứ nhất:")
frac1.inputFraction()

print("\nNhập phân số thứ hai:")
frac2.inputFraction()

print("\n--- Thông tin phân số ---")
print("Phân số 1: ", end="")
frac1.displayFraction()
print("Phân số 2: ", end="")
frac2.displayFraction()

print("\n--- Rút gọn ---")
frac1_simplified = Fraction(frac1.numerator, frac1.denominator)
frac1_simplified.simplify()
print("Phân số 1 rút gọn: ", end="")
frac1_simplified.displayFraction()

print("\n--- Nghịch đảo ---")
try:
    frac1_reciprocal = frac1.reciprocal()
    print("Nghịch đảo phân số 1: ", end="")
    frac1_reciprocal.displayFraction()
except ValueError as e:
    print(f"Lỗi: {e}")

print("\n--- Phép tính ---")
result_add = frac1.add(frac2)
print("Cộng: ", end="")
result_add.displayFraction()

result_sub = frac1.subtract(frac2)
print("Trừ: ", end="")
result_sub.displayFraction()

result_mul = frac1.multiply(frac2)
print("Nhân: ", end="")
result_mul.displayFraction()

try:
    result_div = frac1.divide(frac2)
    print("Chia: ", end="")
    result_div.displayFraction()
except ValueError as e:
    print(f"Lỗi chia: {e}")

print("\nThoát chương trình.")
