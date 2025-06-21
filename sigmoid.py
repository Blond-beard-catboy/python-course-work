#program for sigmoid function

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 100)
def sigmoid(alpha):
    return 1 / ( 1 + np.exp(- alpha * x))

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi))
plt.plot(x, sigmoid(0.5), color='red')
plt.plot(x, sigmoid(1.0), color='blue')
plt.plot(x, sigmoid(2.0), color='green')
plt.plot(x, sigmoid(3.0), color='yellow')
plt.plot(x, sigmoid(10.0), color='cyan')
plt.legend(['A = 0.5', 'A = 1.0', 'A = 2.0', 'A = 3.0', 'A = 10.0'], loc = 'upper left')
plt.title('Сигмоида')
plt.show()
