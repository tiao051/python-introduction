class Student:
    def __init__(self):
        self._student_id = ""
        self._avg_score = 0.0
        self._age = 0
        self._class = ""
    
    @property
    def student_id(self):
        return self._student_id
    
    @property
    def avg_score(self):
        return self._avg_score
    
    @property
    def age(self):
        return self._age
    
    @property
    def class_name(self):
        return self._class
    
    @student_id.setter
    def student_id(self, value):
        self._validate_student_id(value)
        self._student_id = value
    
    @avg_score.setter
    def avg_score(self, value):
        self._validate_avg_score(value)
        self._avg_score = float(value)
    
    @age.setter
    def age(self, value):
        self._validate_age(value)
        self._age = int(value)
    
    @class_name.setter
    def class_name(self, value):
        self._validate_class(value)
        self._class = value

    def _validate_student_id(self, student_id):
        if len(student_id) != 10:
            raise ValueError("Mã số sinh viên phải có 10 ký tự")
        return True
    
    def _validate_avg_score(self, score):
        try:
            score = float(score)
            if score < 0 or score > 10:
                raise ValueError("Điểm trung bình phải từ 0 đến 10")
            return True
        except ValueError:
            raise ValueError("Điểm trung bình phải là số")
    
    def _validate_age(self, age):
        try:
            age = int(age)
            if age < 18:
                raise ValueError("Tuổi phải lớn hơn hoặc bằng 18")
            return True
        except ValueError:
            raise ValueError("Tuổi phải là số nguyên")
    
    def _validate_class(self, class_name):
        if len(class_name) != 8:
            raise ValueError("Lớp phải có 8 ký tự (ví dụ: 12DHTH02)")
        
        if not class_name.startswith("12DH"):
            raise ValueError("Lớp phải bắt đầu với '12DH'")
        
        major = class_name[4:7]
        if major not in ["TH", "MMT"]:
            raise ValueError("Chuyên ngành phải là 'TH' hoặc 'MMT'")
        
        if major == "TH" and len(class_name) != 8:
            raise ValueError("Format lớp sai")
        if major == "MMT" and len(class_name) != 9:
            if len(class_name) == 8:
                raise ValueError("Format lớp sai cho chuyên ngành MMT")
        
        class_number = class_name[7:9] if len(class_name) == 9 else class_name[6:8]
        try:
            num = int(class_number)
            if num < 1 or num > 99:
                raise ValueError("Số lớp phải từ 01 đến 99")
        except ValueError:
            raise ValueError("Số lớp phải là 2 chữ số")
        
        return True
    
    def inputInfo(self):
        while True:
            try:
                student_id = input("Nhập mã số sinh viên (10 ký tự): ")
                self._validate_student_id(student_id)
                self._student_id = student_id
                break
            except ValueError as e:
                print(f"Lỗi: {e}")
        
        while True:
            try:
                score = input("Nhập điểm trung bình (0-10): ")
                self._validate_avg_score(score)
                self._avg_score = float(score)
                break
            except ValueError as e:
                print(f"Lỗi: {e}")
        
        while True:
            try:
                age = input("Nhập tuổi (>= 18): ")
                self._validate_age(age)
                self._age = int(age)
                break
            except ValueError as e:
                print(f"Lỗi: {e}")
        
        while True:
            try:
                class_name = input("Nhập lớp (ví dụ: 12DHTH02): ")
                self._validate_class(class_name)
                self._class = class_name
                break
            except ValueError as e:
                print(f"Lỗi: {e}")
    
    def showInfo(self):
        print(f"Mã số sinh viên: {self.student_id}")
        print(f"Điểm trung bình: {self.avg_score}")
        print(f"Tuổi: {self.age}")
        print(f"Lớp: {self.class_name}")
        print(f"Học bổng: {self._check_scholarship()}")
    
    def _check_scholarship(self):
        if self.avg_score >= 8:
            return "Có"
        else:
            return "Không"

student = Student()

student.inputInfo()
print()
student.showInfo()

print("\nThoát chương trình.")
