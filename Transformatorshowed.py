import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

plt.style.use('_mpl-gallery')

# Crear los datos
X = np.linspace(-np.pi, np.pi, 100)
Y = np.linspace(-np.pi, np.pi, 100)
X, Y = np.meshgrid(X, Y)

Z = 1 + 2 * np.cos(X) + 2 * np.cos(Y) + 2 * np.cos(X + Y) + 2 * np.cos(X - Y)

# Crear la figura y los ejes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Crear la superficie
surf = ax.plot_surface(X, Y, Z, cmap=cm.Greens, vmin=Z.min() * 2)

# Ocultar etiquetas de los ejes
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_zticklabels([])

# Mostrar la gráfica
plt.show()
