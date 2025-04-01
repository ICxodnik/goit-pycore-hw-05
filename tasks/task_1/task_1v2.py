def get_fibonacci_range():
    cache = {0: 0, 1: 1}  # Початкові значення Фібоначчі

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n in cache:
            return cache[n]

        for i in range(len(cache), n + 1):
            cache[i] = cache[i - 1] + cache[i - 2]
            yield cache[i]  # Генеруємо та кешуємо нове число

    return fibonacci


if __name__ == "__main__":
    fib = get_fibonacci_range()
    
    # Отримуємо генератор для 10-го числа Фібоначчі
    for num in fib(10):
        pass  # Прокручуємо генератор до останнього значення
    
    print(num)  # Виведе 55
    
    # Отримуємо генератор для 15-го числа Фібоначчі
    for num in fib(15):
        pass  
    
    print(num)  # Виведе 610
