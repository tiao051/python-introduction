class StringHandler:
    def __init__(self):
        self._string = ""
    
    @property
    def string(self):
        return self._string
    
    @string.setter
    def string(self, value):
        self._string = value
    
    def get(self):
        self._string = input("Nhập một chuỗi: ")
    
    def put(self):
        print(f"Chuỗi: {self.string}")

handler = StringHandler()

handler.get()
handler.put()

print("\nThoát chương trình.")
