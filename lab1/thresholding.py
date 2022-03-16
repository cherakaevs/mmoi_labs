import numpy as np
from matplotlib import pyplot as plt


def thresholding(img, threshold=100):
    grayscale = img
    grayscale = np.where(img <= threshold, grayscale, 0)
    grayscale = np.where(img > threshold, grayscale, 255)

    plt.title("График функции поэлементного преобразования")
    plt.xlabel("f")
    plt.ylabel("g")
    x = np.arange(0, 256)
    x = np.where(x > threshold, x, 0)
    x = np.where(x <= threshold, x, 255)
    plt.plot(x)
    return grayscale
