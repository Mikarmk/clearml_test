def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Введите число: "))
print(f"Факториал числа {number} равен {factorial(number)}")
