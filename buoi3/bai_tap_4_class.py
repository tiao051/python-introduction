class Employee:
    def __init__(self):
        self._name = ""
        self._age = 0
        self._address = ""
        self._salary = 0.0
        self._total_hours = 0
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def address(self):
        return self._address
    
    @property
    def salary(self):
        return self._salary
    
    @property
    def total_hours(self):
        return self._total_hours
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @age.setter
    def age(self, value):
        self._age = value
    
    @address.setter
    def address(self, value):
        self._address = value
    
    @salary.setter
    def salary(self, value):
        self._salary = value
    
    @total_hours.setter
    def total_hours(self, value):
        self._total_hours = value

    def inputInfo(self):
        self._name = input("Nhập tên nhân viên: ")
        self._age = int(input("Nhập tuổi: "))
        self._address = input("Nhập địa chỉ: ")
        self._salary = float(input("Nhập tiền lương: "))
        self._total_hours = int(input("Nhập tổng số giờ làm: "))
    
    def printInfo(self):
        print(f"Tên: {self.name}")
        print(f"Tuổi: {self.age}")
        print(f"Địa chỉ: {self.address}")
        print(f"Tiền lương: {self.salary:.2f}")
        print(f"Tổng số giờ làm: {self.total_hours}")
        print(f"Tiền thưởng: {self.tinhThuong():.2f}")
    
    def tinhThuong(self):
        if self.total_hours >= 200:
            return self.salary * 0.2
        elif self.total_hours >= 100:
            return self.salary * 0.1
        else:
            return 0

employee = Employee()

employee.inputInfo()
print()
employee.printInfo()

print("\nThoát chương trình.")
