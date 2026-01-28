class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Error"
        
    def input_numbers(self):
        self.a = float(input("Enter the first number: "))
        self.b = float(input("Enter the second number: "))

    def show_numbers(self):
        print("First number: {}".format(self.a))
        print("Second number: {}".format(self.b))
    
calc = Calculator(0, 0)

choice = 1
while choice != 0:
    print("0. Exit")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Your choice: "))
    
    match choice:
        case 0:
            print("Goodbye!")
            break
        case 1:
            calc.input_numbers()
            calc.show_numbers()
            print("Result: {}".format(calc.add()))
        case 2:
            calc.input_numbers()
            calc.show_numbers()
            print("Result: {}".format(calc.subtract()))
        case 3:
            calc.input_numbers()
            calc.show_numbers()
            print("Result: {}".format(calc.multiply()))
        case 4:
            calc.input_numbers()
            calc.show_numbers()
            print("Result: {}".format(calc.divide()))
        case _:
            print("Invalid choice. Please try again.\n")
