import numpy as np
import matplotlib.pyplot as plt

# Параметри варіанту №6
N = 6
H = 1000 - N
beta = 25 - N         # інтенсивність передачі
gamma_days = N        # середня кількість днів до одужання
gamma = 1 / gamma_days  # швидкість одужання (1/γ)

# Початкові умови
x0 = 900 - N  # здорові
y0 = 90 - N   # хворі
z0 = H - x0 - y0  # перехворіли

# Часова сітка
t0, T, h = 0, 40, 0.1
t = np.arange(t0, T + h, h)
n = len(t)

# Масиви для розв'язку
x = np.zeros(n)
y = np.zeros(n)
z = np.zeros(n)
x[0], y[0], z[0] = x0, y0, z0

# Функція правих частин
def f(vars):
    xi, yi, zi = vars
    dx = - beta * xi * yi / H
    dy = beta * xi * yi / H - gamma * yi
    dz = gamma * yi
    return np.array([dx, dy, dz])

# Метод Рунге-Кутта 4-го порядку
for i in range(n - 1):
    vars_i = np.array([x[i], y[i], z[i]])
    k1 = f(vars_i)
    k2 = f(vars_i + 0.5 * h * k1)
    k3 = f(vars_i + 0.5 * h * k2)
    k4 = f(vars_i + h * k3)
    vars_next = vars_i + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
    x[i+1], y[i+1], z[i+1] = vars_next

# Графік
plt.figure()
plt.plot(t, x, label='Здорові x(t)')
plt.plot(t, y, label='Хворі y(t)')
plt.plot(t, z, label='Імунітет z(t)')
plt.xlabel('Час (дні)')
plt.ylabel('Кількість людей')
plt.legend()
plt.title('Динаміка SIR-моделі з γ = 1/6')
plt.show()
