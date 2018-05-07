import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from skimage import measure, io
from skimage.filters import threshold_otsu, sobel
from skimage.color import rgb2gray
from skimage.transform import (hough_line, hough_line_peaks, probabilistic_hough_line, rotate)
from skimage.feature import canny
from skimage.morphology import binary_dilation
from scipy.stats import mode
import math
import sys


def objective_function_projection(img):
    projection = np.sum(img, axis=1)
    diffs = np.diff(projection)
    return np.square(diffs).sum()


def find_rotation_angle_projection(input_image_file):
    img = io.imread(input_image_file)
    img = rgb2gray(img)
    thresh = threshold_otsu(img)
    img = img > thresh  # binarize

    plt.imshow(img, cmap='gray')
    save_image('projection1_' + input_image_file, input_image_file)

    angles = np.arange(-90.0, 90.0, 1.0)
    costs = np.empty((len(angles), 2))
    i = 0
    for angle in angles:
        rotated_img = rotate(img, angle, cval=1)
        costs[i][0] = angle
        costs[i][1] = objective_function_projection(rotated_img)
        i += 1

    print("file:", input_image_file)

    print("max objective function: ", costs[costs.argmax(axis=0)[1]])
    plt.plot(costs[:, 0], costs[:, 1])
    save_image('projection2_' + input_image_file, input_image_file)

    # get angle with max objective function value
    return costs[costs.argmax(axis=0)[1]][0]


def objective_function_hough(img):
    h, theta, d = hough_line(img)
    hspace, angles, dists = hough_line_peaks(h, theta, d)

    most_common_theta = np.rad2deg(mode(angles)[0][0])  # theta in degrees

    if most_common_theta > 0:
        text_angle = -90 + most_common_theta
    else:
        text_angle = 90 + most_common_theta

    print("top in degrees:", text_angle)
    return text_angle  # convert from radians to degrees


def find_rotation_angle_hough(input_image_file):
    image = io.imread(input_image_file)
    image = rgb2gray(image)

    # binarize image
    thresh = threshold_otsu(image)
    image = image > thresh  # binarize

    # apply sobel filter
    image = sobel(image)
    image = -image
    image = binary_dilation(image)
    print("file:", input_image_file)

    angle_rotation = objective_function_hough(image)
    print("angle_rotation: ", angle_rotation)

    h, theta, d = hough_line(image)
    # Generating figure 1
    fig, axes = plt.subplots(2, 2, figsize=(20, 12))
    ax = axes.ravel()

    ax[0].imshow(image, cmap=cm.gray)
    ax[0].set_title('Input image')
    ax[0].set_axis_off()

    ax[1].imshow(np.log(1 + h),
                 extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), d[-1], d[0]],
                 cmap=cm.gray)
    ax[1].set_title('Hough transform')
    ax[1].set_xlabel('Angles (degrees)')
    ax[1].set_ylabel('Distance (pixels)')
    ax[1].axis('image')

    hspace, angles, dists = hough_line_peaks(h, theta, d)
    print(angles)

    ax[2].imshow(image, cmap=cm.gray)
    for _, angle, dist in zip(*hough_line_peaks(h, theta, d)):
        y0 = (dist - 0 * np.cos(angle)) / np.sin(angle)
        y1 = (dist - image.shape[1] * np.cos(angle)) / np.sin(angle)
        ax[2].plot((0, image.shape[1]), (y0, y1), '-r')
    ax[2].set_xlim((0, image.shape[1]))
    ax[2].set_ylim((image.shape[0], 0))
    ax[2].set_axis_off()
    ax[2].set_title('Detected lines')

    fixed_image = rotate(io.imread(input_image_file), angle_rotation)
    ax[3].imshow(fixed_image, cmap=cm.gray)
    ax[2].set_axis_off()
    ax[2].set_title('Fixed image')

    plt.tight_layout()
    save_image('hough_' + input_image_file, input_image_file)

    return angle_rotation


def save_image(filename, title, axis='off'):
    '''
    Saves to file whatever we have plotted to matplotlib so far
    :param filename: output file saved
    :param title: title of the plot
    :return: None
    '''
    plt.axis(axis)
    plt.title(title)

    plt.savefig(filename)
    plt.clf()


def main():
    '''
    Usage: python3 alinhar.py imagem_entrada.png <h|p> imagem_saida.png
    '''
    input_image_file = sys.argv[1]
    mode = sys.argv[2]
    output_image_file = sys.argv[3]

    if mode == 'h':
        angle = find_rotation_angle_hough(input_image_file)
    elif mode == 'p':
        angle = find_rotation_angle_projection(input_image_file)
    else:
        print("Bad parameters")
        print("Usage: python3 alinhar.py imagem_entrada.png <h|p> imagem_saida.png")
        print("Try again :)")

    # fix text orientation
    fixed_image = rotate(io.imread(input_image_file), angle)
    io.imsave(output_image_file, fixed_image)


if __name__ == "__main__":
    main()

