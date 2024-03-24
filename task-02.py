import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа
n = 100000  # Кількість випадкових точок

# Генерування випадкових точок всередині прямокутника
x_rand = np.random.uniform(a, b, n)
y_rand = np.random.uniform(0, f(b), n)

# Обчислення кількості точок, які потрапили під криву
count_under_curve = np.sum(y_rand <= f(x_rand))

# Обчислення значення інтеграла методом Монте-Карло
integral_approx = count_under_curve / n * (b - a) * f(b)

print("Значення інтеграла методом Монте-Карло:", integral_approx)

# Обчислення інтеграла аналітично
result, _ = spi.quad(f, a, b)
print("Значення інтеграла за допомогою quad:", result)
