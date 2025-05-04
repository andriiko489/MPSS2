import matplotlib.pyplot as plt

N = 6
a11 = 0.01 * N
a12 = 0.0001 * N
a21 = 0.0001 * N
a22 = 0.04 * N

x0 = 1000 - 10 * N  # початкова кількість жертв
y0 = 700 - 10 * N   # початкова кількість хижаків

t0 = 0
T = 150
h = 0.1
steps = int((T - t0) / h) + 1

# Рівняння Лотка-Вольтера
def dx_dt(x, y): return x * (a11 - a12 * y)
def dy_dt(x, y): return -y * (a22 - a21 * x)

# Метод Рунге-Кутта 4-го порядку
x_vals, y_vals, t_vals = [x0], [y0], [t0]

for _ in range(steps):
    x, y = x_vals[-1], y_vals[-1]

    k1x = h * dx_dt(x, y)
    k1y = h * dy_dt(x, y)

    k2x = h * dx_dt(x + 0.5 * k1x, y + 0.5 * k1y)
    k2y = h * dy_dt(x + 0.5 * k1x, y + 0.5 * k1y)

    k3x = h * dx_dt(x + 0.5 * k2x, y + 0.5 * k2y)
    k3y = h * dy_dt(x + 0.5 * k2x, y + 0.5 * k2y)

    k4x = h * dx_dt(x + k3x, y + k3y)
    k4y = h * dy_dt(x + k3x, y + k3y)

    x_next = x + (k1x + 2 * k2x + 2 * k3x + k4x) / 6
    y_next = y + (k1y + 2 * k2y + 2 * k3y + k4y) / 6

    x_vals.append(x_next)
    y_vals.append(y_next)
    t_vals.append(t_vals[-1] + h)

# Побудова графіків
plt.figure(figsize=(15, 4))
plt.subplot(1, 3, 1)
plt.plot(t_vals, x_vals, label='Жертви x(t)')
plt.plot(t_vals, y_vals, label='Хижаки y(t)')
plt.xlabel("Час (дні)")
plt.ylabel("Кількість")
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(x_vals, y_vals)
plt.xlabel("Жертви x")
plt.ylabel("Хижаки y")
plt.title("Фазова траєкторія y(x)")

plt.tight_layout()
plt.show()
