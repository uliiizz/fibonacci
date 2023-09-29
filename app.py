def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            next_number = fib_series[i - 1] + fib_series[i - 2]
            fib_series.append(next_number)
        return fib_series
n = int(input("Введіть кількість чисел Фібоначчі: "))
result = fibonacci(n)
print("Числа Фібоначчі:", result)
