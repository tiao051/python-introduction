from datetime import datetime

class Person:
    def __init__(self):
        self._name = ""
        self._country = ""
        self._date_of_birth = ""
    
    @property
    def name(self):
        return self._name
    
    @property
    def country(self):
        return self._country
    
    @property
    def date_of_birth(self):
        return self._date_of_birth
    
    def _validate_date(self, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            raise ValueError("Ngày sinh phải có định dạng YYYY-MM-DD")
    
    def inputInfo(self):
        self._name = input("Nhập tên: ")
        self._country = input("Nhập quốc gia: ")
        
        while True:
            try:
                date_str = input("Nhập ngày sinh (YYYY-MM-DD): ")
                self._validate_date(date_str)
                self._date_of_birth = date_str
                break
            except ValueError as e:
                print(f"Lỗi: {e}")
    
    def getAge(self):
        birth_date = datetime.strptime(self.date_of_birth, "%Y-%m-%d")
        today = datetime.now()
        age = today.year - birth_date.year
        
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def displayInfo(self):
        print(f"Tên: {self.name}")
        print(f"Quốc gia: {self.country}")
        print(f"Ngày sinh: {self.date_of_birth}")
        print(f"Tuổi: {self.getAge()}")

person = Person()

person.inputInfo()
print()
person.displayInfo()

print("\nThoát chương trình.")
