import numpy as np
import matplotlib.pyplot as plt

# def mass(x):
#     density = 0
#     volume = 0
#     for i in range(x):
#         x_axis = np.random.uniform(0,1)
#         y_axis = np.random.uniform(0,1)
#         if y_axis >= x_axis**2:
#             volume += 1-(x_axis**2)
#             density += (20/13)*(x_axis + y_axis)
#         else:
#             continue
#     z = density*volume
#     return z

incidents = 1000

x_axis = np.arange(0, 1, 0.0001)
x = np.random.uniform(0,1)
y = np.random.uniform(0,1)
for i in range(incidents):
    if y >= x**2:
        density =+ (20/13)*(x + y)
        j =+ 1
    else:
        continue

print(j)
plt.plot(density)
plt.show()
