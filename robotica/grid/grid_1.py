import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.draw import line

fig = plt.figure(figsize=(8,8), dpi=100)
ax = fig.add_subplot(111, aspect='equal')

map_size = np.array([20, 20])
cell_size = 1

rows, cols = (map_size/cell_size).astype(int)

m = np.random.uniform(low=0.0, high=1.0, size=(rows, cols))

m[0,0] = 1 
plt.imshow(m, cmap='Greys', origin='upper', extent=(0, cols, rows, 0))

ax.set_xticks(np.arange(0, cols, cell_size))
ax.set_yticks(np.arange(0, rows, cell_size))

plt.colorbar()
plt.show()

x, y = 5.5, 5.5
xo, yo = 15.5, 10.5

# x: column, y: row
xi, yi = np.floor((1/cell_size)*np.array([x, y])).astype(int)
xoi, yoi = np.floor((1/cell_size)*np.array([xo, yo])).astype(int)

line_bresenham = np.zeros((rows, cols), dtype=np.uint8)
rr, cc = line(yi, xi, yoi, xoi) # r0, c0, r1, c1
line_bresenham[rr, cc] = 1

fig = plt.figure(figsize=(8,8), dpi=100)
ax = fig.add_subplot(111, aspect='equal')

ax.imshow(m, cmap='Greys', extent=(0, cols, rows, 0))
ax.imshow(line_bresenham, cmap='Reds', extent=(0, cols, rows, 0), alpha=.5)

ax.set_xticks(np.arange(0, cols, cell_size))
ax.set_yticks(np.arange(0, rows, cell_size))

ax.plot([x, xo], [y, yo], 'r-', linewidth=3)

plt.show()
