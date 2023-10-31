import numpy as np
from matplotlib import pyplot as plt

x = [x for x in range(0, 100)]
y = np.sin(x) * np.cos(x)

plt.plot(x, y, '-')
plt.fill_between(x, y, 195, where=(y > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()