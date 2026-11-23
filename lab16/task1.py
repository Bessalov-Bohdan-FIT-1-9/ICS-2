import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.3, 12.3, 200)
y = np.log(x) + 0.7 * x ** 2

plt.plot(x, y, 'c--', label='y = ln(x) + 0.7x^2')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Графік функції y = ln(x) + 0.7x^2')
plt.grid(True)
plt.legend()

plt.show()
plt.savefig('myplot.jpg', dpi=300)