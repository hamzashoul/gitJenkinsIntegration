import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z * z + c
        n += 1
    return n

def generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    mandelbrot_set = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            c = complex(real[i], imag[j])
            mandelbrot_set[i, j] = mandelbrot(c, max_iter)
    
    return mandelbrot_set

# Parameters for the Mandelbrot set
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 800, 800
max_iter = 256

# Generate the Mandelbrot set
mandelbrot_image = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plotting the Mandelbrot set
plt.imshow(mandelbrot_image.T, extent=[xmin, xmax, ymin, ymax], cmap='inferno', interpolation='bilinear')
plt.colorbar()
plt.title("Mandelbrot Set")
plt.xlabel("Re")
plt.ylabel("Im")
plt.show()
