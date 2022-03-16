import numpy as np
from matplotlib import pyplot as plt


def linear_contrast(img, fmin, fmax, gmin=0, gmax=255):
    a = (gmax - gmin) / (fmax - fmin)
    b = ((gmin * fmax) - (gmax * fmin)) / (fmax - fmin)

    x = np.arange(0, 256)

    plt.title("График функции поэлементного преобразования")
    plt.xlabel("f")
    plt.ylabel("g")
    x = x * a + b
    x = np.where(x > gmin, x, 0)
    x = np.where(x <= gmax, x, 255)
    plt.grid()
    plt.plot(x)

    lc = (img * a + b).astype(np.uint8)
    return lc
