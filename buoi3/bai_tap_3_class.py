class SubsetGenerator:
    def __init__(self):
        self._numbers = []
        self._subsets = []
    
    @property
    def numbers(self):
        return self._numbers
    
    @property
    def subsets(self):
        return self._subsets
    
    def f1(self):
        numbers_input = input("Nhập các số nguyên cách nhau bằng khoảng trắng: ")
        self._numbers = list(map(int, numbers_input.split()))
        self.f2()
    
    def f2(self):
        self._subsets = [[]]
        
        for num in self._numbers:
            new_subsets = [subset + [num] for subset in self._subsets]
            self._subsets += new_subsets
    
    def display(self):
        print(f"Danh sách: {self.numbers}")
        print(f"Tất cả các tập hợp con:")
        for subset in self.subsets:
            print(subset)

generator = SubsetGenerator()

generator.f1()
generator.display()

print("\nThoát chương trình.")
