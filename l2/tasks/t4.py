a = int(input("Введите первое число: "))
oper = input("Введите операцию: ")
b = int(input("Введите второе число: "))
match oper:
    case "+":
        print(f"Ответ: {a + b}")
    case "-":
        print(f"Ответ: {a - b}")
    case "*":
        print(f"Ответ: {a * b}")
    case "/":
        if b != 0:
            print(f"Ответ: {a / b}")
        else: print("error")