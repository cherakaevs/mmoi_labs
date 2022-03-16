import sys

from matplotlib import pyplot as plt
from skimage.io import imshow, show, imread

import thresholding, lc, equalization

PATH = "/Users/karmikfeels/PycharmProjects/mmoi_labs/lab1/09_lena2.tif"


def output(img, proc_img):
    fig = plt.figure(figsize=(10, 6))
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
    out_img = ''

    if mode == "THRESHOLD":
        out_img = thresholding.thresholding(img)
    if mode == "CONTRAST":
        out_img = lc.linear_contrast(img, img.min(), img.max())
    if mode == "EQUALIZE":
        out_img = equalization.equalize(img, 0, 255)

    output(img, out_img)


if __name__ == "__main__":
    run("THRESHOLD")
    run("CONTRAST")
    run("EQUALIZE")
    sys.exit()
