from matplotlib import pyplot as plt
import numpy as np
x = np.arange(1,10,.01)
y = np.sinh(x)
plt.plot(x,y)

save_file_ = 'wall.png'

plt.savefig(save_file_)
print("Plot saved as "+save_file_)
# plt.show()
