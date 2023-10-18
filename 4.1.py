class Calculator:
    def __init__(self):
        pass
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b==0:
            return "Деление на ноль невозможно"
        return a/b
    def get_input(self):
        try:
                num1=float(input("Введите первое число"))
                num2=float(input("Введите второе число:"))
        except ValueError:
            print("Введите цифру")
        while True:
            print("Выберите действие:")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Выход")
            ch=input("Введите номер:")
            if ch=='5':
                break
            if ch=='1':
                res=self.add(num1,num2)
                print(f"{num1} + {num2} = {res}")
            elif ch=='2':
                res=self.subtract(num1,num2)
                print(f"{num1} - {num2} = {res}")
            elif ch=='3':
                res=self.multiply(num1,num2)
                print(f"{num1} * {num2} = {res}")
            elif ch=='4':
                res=self.divide(num1,num2)
                print(f"{num1} / {num2} = {res}")
            else:
                print("Неверный ввод")
calc=Calculator()
calc.get_input()