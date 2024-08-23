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
width, height = 1000, 1000
max_iter = 512
cmap = 'inferno'  # Choose different color maps: 'viridis', 'plasma', 'inferno', 'magma', 'cividis'

# Generate the Mandelbrot set
mandelbrot_image = generate_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plotting the Mandelbrot set with the selected color map
plt.imshow(mandelbrot_image.T, extent=[xmin, xmax, ymin, ymax], cmap=cmap, interpolation='bilinear')
plt.colorbar()
plt.title("Mandelbrot Set (Zoom: [{}, {}] x [{}, {}])".format(xmin, xmax, ymin, ymax))
plt.xlabel("Re")
plt.ylabel("Im")

# Save the image to a file
output_filename = 'mandelbrot_set.png'
plt.savefig(output_filename, dpi=300)
print(f"Mandelbrot set image saved as {output_filename}")

plt.show()
