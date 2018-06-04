#
# Exercicio 4
# MO443 - Processamento de Imagens
# Prof. Helio Pedrini 1o. sem 2018
# Aluno: Edgar Tanaka
# RA: 023577
#
import matplotlib
matplotlib.use('Agg')
import argparse
import math
import matplotlib
import numpy as np
import sys
from matplotlib import cm
from matplotlib import pyplot as plt
from skimage import measure, io


def calculate_dx_dy(indexes):
    dx_dy = indexes - np.floor(indexes)
    return dx_dy[0], dx_dy[1]


def l_function(n, dx, x, y, original_img):
    width = original_img.shape[0] - 1
    height = original_img.shape[1] - 1
    y = np.clip(y + n - 2, 0, height)  # y + n - 2
    l_value = (-dx * (dx - 1) * (dx - 2) * original_img[np.clip(x - 1, 0, width), y]) / 6
    l_value += ((dx + 1) * (dx - 1) * (dx - 2) * original_img[x, y]) / 2
    l_value += (-dx * (dx + 1) * (dx - 2) * original_img[np.clip(x + 1, 0, width), y]) / 2
    l_value += (dx * (dx + 1) * (dx - 1) * original_img[np.clip(x + 2, 0, width), y]) / 6
    return l_value


def interpolate_lagrange(indexes, original_img):
    dx, dy = calculate_dx_dy(indexes)
    x = np.floor(indexes[0]).astype(int)
    y = np.floor(indexes[1]).astype(int)
    scaled_img = (-dy * (dy - 1) * (dy - 2) * l_function(1, dx, x, y, original_img)) / 6
    scaled_img += ((dy + 1) * (dy - 1) * (dy - 2) * l_function(2, dx, x, y, original_img)) / 2
    scaled_img += (-dy * (dy + 1) * (dy - 2) * l_function(3, dx, x, y, original_img)) / 2
    scaled_img += (dy * (dy + 1) * (dy - 1) * l_function(4, dx, x, y, original_img)) / 6
    return scaled_img.astype(int)


def r_function(s):
    return ((np.maximum(s + 2, 0) ** 3) - 4 * (np.maximum(s + 1, 0) ** 3) + 6 * (np.maximum(s, 0) ** 3) - 4 * (
                np.maximum(s - 1, 0) ** 3)) / 6


def interpolate_bicubic(indexes, original_img):
    dx, dy = calculate_dx_dy(indexes)
    scaled_img = np.zeros(dx.shape)
    width = original_img.shape[0] - 1
    height = original_img.shape[1] - 1

    for m in range(-1, 3):
        for n in range(-1, 3):
            r2 = r_function(m - dx)
            r1 = r_function(dy - n)
            x = np.floor(indexes[0]).astype(int)
            y = np.floor(indexes[1]).astype(int)
            x = np.clip(x + m, 0, width)
            y = np.clip(y + n, 0, height)
            scaled_img += r1 * r2 * original_img[x, y]

    return scaled_img.astype(int)


def interpolate_bilinear(indexes, original_img):
    width = original_img.shape[0] - 1
    height = original_img.shape[1] - 1

    dx, dy = calculate_dx_dy(indexes)
    scaled_img = np.zeros(dx.shape)
    x = np.floor(indexes[0]).astype(int)
    y = np.floor(indexes[1]).astype(int)

    scaled_img += (1 - dx) * (1 - dy) * original_img[np.clip(x, 0, width), np.clip(y, 0, height)]
    scaled_img += dx * (1 - dy) * original_img[np.clip(x + 1, 0, width), np.clip(y, 0, height)]
    scaled_img += (1 - dx) * dy * original_img[np.clip(x, 0, width), np.clip(y + 1, 0, height)]
    scaled_img += dx * dy * original_img[np.clip(x + 1, 0, width), np.clip(y + 1, 0, height)]

    return scaled_img.astype(int)


def interpolate_nn(indexes, original_img):
    indexes = np.round(indexes).astype(int)
    width = original_img.shape[0] - 1
    height = original_img.shape[1] - 1
    x = indexes[0]
    y = indexes[1]
    return original_img[np.clip(x, 0, width), np.clip(y, 0, height)]


def interpolate(method, indexes, original_img):
    if method == 4:
        return interpolate_lagrange(indexes, original_img)
    elif method == 3:
        return interpolate_bicubic(indexes, original_img)
    elif method == 2:
        return interpolate_bilinear(indexes, original_img)
    else:
        return interpolate_nn(indexes, original_img)


def rotate_image(method, original_img, theta):
    """
    Rotates an image while maintaining the center of the image.
    :param method:
    :param original_img:
    :param theta: in degrees
    :return: matrix with rotated image
    """
    theta = np.deg2rad(theta)
    indexes = np.indices(original_img.shape)

    x = indexes[0]
    y = indexes[1]
    w = original_img.shape[0]
    h = original_img.shape[1]
    x_ = (x * math.cos(theta)) - (y * math.sin(theta))
    y_ = (x * math.sin(theta)) + (y * math.cos(theta))

    # calculate offset to center the image
    center_x = ((w / 2) * math.cos(theta)) - ((h / 2) * math.sin(theta))
    center_y = ((w / 2) * math.sin(theta)) + ((h / 2) * math.cos(theta))
    offset_x = (w / 2) - center_x
    offset_y = (h / 2) - center_y

    # center image
    x_ += offset_x
    y_ += offset_y

    # clip to values in image range
    x = np.clip(x_, 0, w - 1).round().astype(int)
    y = np.clip(y_, 0, h - 1).round().astype(int)

    # filter out invalid coordinates (out of bounds)
    filter_invalid_coordinates = np.logical_or(
        np.logical_or(x_ > w - 1, y_ > h - 1),
        np.logical_or(x_ < 0, y_ < 0)
    )

    # calculate dx and dy
    indexes[0] = x
    indexes[1] = y

    rotated_img = interpolate(method, indexes, original_img)

    # paint areas out of image range as black
    rotated_img[filter_invalid_coordinates] = 0
    return rotated_img


def scale_image(method, original_img, scale):
    scaled_shape = np.multiply(original_img.shape, scale).astype(int)
    return resize_image(method, original_img, scaled_shape[0], scaled_shape[1])


def resize_image(method, original_img, width, height):
    scale_x = width / original_img.shape[0]
    scale_y = height / original_img.shape[1]

    # resize
    indexes = np.indices((width, height))
    indexes[0] = indexes[0] / scale_x
    indexes[1] = indexes[1] / scale_y

    return interpolate(method, indexes, original_img)


def main():
    parser = argparse.ArgumentParser(description='Scale and Rotate image.')
    parser.add_argument('-a', type=float, help='angle')
    parser.add_argument('-e', type=float, help='scale')
    parser.add_argument('-d', type=int, help='width and height', nargs=2)
    parser.add_argument('-m', type=int, help='interpolation method', choices=range(1, 5))
    parser.add_argument('-i', help='input image')
    parser.add_argument('-o', help='output image')

    args = parser.parse_args()

    input_img_file = args.i
    output_img_file = args.o
    method = args.m
    angle = args.a
    scale = args.e
    dimensions = args.d

    # read image
    original_img = io.imread(input_img_file, as_grey=True)
    print("original img shape:", original_img.shape)

    # apply transformation
    if angle:
        output_img = rotate_image(method, original_img, angle)
    elif scale:
        output_img = scale_image(method, original_img, scale)
    elif dimensions:
        width = dimensions[0]
        height = dimensions[1]
        output_img = resize_image(method, original_img, width, height)

    # save output image
    io.imsave(output_img_file, output_img, cmap='gray', vmin=0, vmax=255)


if __name__ == "__main__":
    main()

