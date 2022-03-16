import sys

import numpy as np
from skimage.exposure import exposure

import equalization
import lc
import thresholding

from matplotlib import pyplot as plt
from skimage.io import imshow, show, imread

PATH = "/Users/karmikfeels/PycharmProjects/mmoi_labs/lab1/09_lena2.tif"


def output(img, proc_img, title):
    fig = plt.figure(figsize=(10, 6))
    plt.title(title)
    fig.add_subplot(2, 2, 1)
    imshow(img)
    fig.add_subplot(2, 2, 2)
    imshow(proc_img / proc_img.max(), cmap=plt.cm.gray)

    fig.add_subplot(2, 2, 3)

    plt.hist(img.ravel(), 256, [0, 256])
    plt.tight_layout(h_pad=1.0)

    fig.add_subplot(2, 2, 4)
    plt.hist(proc_img.ravel(), 256, [0, 256])
    plt.tight_layout(h_pad=1.5)

    fig.tight_layout()
    show()


def run(mode):
    img = imread(PATH)

    if mode == "THRESHOLD":
        out_img = thresholding.thresholding(img)
        t = "Пороговая обработка"
        output(img, out_img, title=t)
    if mode == "CONTRAST":
        out_img = lc.linear_contrast(img, img.min(), img.max())
        t = "Линейное контрастирование"
        output(img, out_img, title=t)
    if mode == "EQUALIZE":
        img = imread(PATH)
        t = "Эквализация гистограмм"
        out_img = equalization.equalize(img, 0, 255)
        output(img, out_img, title="Стандартная эквализация")
        eq = (exposure.equalize_hist(img) * 255).astype(np.uint8)
        out_h = np.histogram(eq, 256, [0, 256])[0]
        out_h = np.cumsum(out_h) / (img.shape[0] * img.shape[1])
        plt.plot(out_h)
        output(img, eq, title=t)


if __name__ == "__main__":
    run("THRESHOLD")
    # run("CONTRAST")
    # run("EQUALIZE")
    sys.exit()
