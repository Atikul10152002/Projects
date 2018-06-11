from matplotlib import pyplot as plt
import numpy as np
x = np.arange(1,10,.01)
y = np.sinh(x)
plt.plot(x,y)

plt.savefig('wall.png')
plt.show()
