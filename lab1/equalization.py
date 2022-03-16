import numpy as np
from matplotlib import pyplot as plt


def equalize(img, gmin=0, gmax=255):
    h = np.histogram(img, 256, [0, 256])[0]
    density = np.cumsum(h) / (img.shape[0] * img.shape[1])

    plt.title("График интегральной функции")
    plt.xlabel("f")
    plt.ylabel("g")
    plt.plot(density)

    f = ((gmax - gmin) * density + gmin).astype(np.uint8)
    eq = f[img]
    out_h, b = np.histogram(eq, 256, [0, 256])
    out_h = np.cumsum(out_h) / (img.shape[0] * img.shape[1])
    plt.plot(out_h)
    return eq
