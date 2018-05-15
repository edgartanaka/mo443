import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from skimage import measure, io
from skimage.filters import threshold_otsu, sobel
from skimage.transform import (hough_line, hough_line_peaks, probabilistic_hough_line, rotate)
from skimage.feature import canny
from skimage.morphology import binary_dilation
from scipy.stats import mode
import math
import sys


def objective_function_projection(img):
    '''
    First sums pixels horizontally.
    Then calculates squared diffs of each cell adjacent.
    :param img:
    :return:
    '''
    projection = np.sum(img, axis=1)
    diffs = np.diff(projection)
    return np.square(diffs).sum()


def find_rotation_angle_projection(input_image_file):
    # pre-processing: binarize image
    original_image = io.imread(input_image_file, as_grey=True)
    thresh = threshold_otsu(original_image)
    pre_processed_image = original_image > thresh

    # calculate objective function for each angle
    angles = np.arange(-90.0, 90.0, 1.0)
    costs = np.empty((len(angles), 2))
    i = 0
    for angle in angles:
        rotated_img = rotate(pre_processed_image, angle, cval=1)
        costs[i][0] = angle
        costs[i][1] = objective_function_projection(rotated_img)
        i += 1

    # get angle with max objective function value
    angle_rotation = costs[costs.argmax(axis=0)[1]][0]

    print('======================================================================================')
    print('Input file:', input_image_file)
    print('Mode: Horizontal Projection')
    print('Angle to rotate:', angle_rotation)
    print('======================================================================================')

    # print analysis of horizontal projection
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    ax = axes.ravel()

    ax[0].imshow(pre_processed_image, cmap=cm.gray)
    ax[0].set_title('Pre-processed image')
    ax[0].set_axis_off()

    ax[1].bar(costs[:, 0], costs[:, 1])
    ax[1].set_xlabel('Angles (degrees)')
    ax[1].set_ylabel('Objective function')
    ax[1].set_title('Horizontal Projection')

    ax[2].imshow(rotate(io.imread(input_image_file), angle_rotation))
    ax[2].set_title('Fixed image')
    ax[2].set_axis_off()

    plt.tight_layout()
    plt.savefig('projection_' + input_image_file)
    plt.clf()

    return angle_rotation


def objective_function_hough(img):
    h, theta, d = hough_line(img)
    hspace, angles, dists = hough_line_peaks(h, theta, d)

    # calculate most common theta from all the peaks
    most_common_theta = np.rad2deg(mode(angles)[0][0])

    # most_common_theta is perpendicular to the text line
    # calculate text_angle which is perpendicular to most_common_theta
    if most_common_theta > 0:
        text_angle = -90 + most_common_theta
    else:
        text_angle = 90 + most_common_theta

    return text_angle


def print_hough_analysis(image, angle_rotation, input_image_file):
    h, theta, d = hough_line(image)
    fig, axes = plt.subplots(1, 4, figsize=(30, 7))
    ax = axes.ravel()

    ax[0].imshow(image, cmap=cm.gray)
    ax[0].set_title('Pre-processed image')
    ax[0].set_axis_off()

    ax[1].imshow(np.log(1 + h),
                 extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), d[-1], d[0]],
                 cmap='jet')
    ax[1].set_title('Hough transform')
    ax[1].set_xlabel('Angles (degrees)')
    ax[1].set_ylabel('Distance (pixels)')
    ax[1].axis('image')
    ax[1].set_aspect(180/(d[-1]-d[0]))

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
    ax[3].set_title('Fixed image')
    ax[3].set_axis_off()

    plt.tight_layout()
    save_image('hough_' + input_image_file)


def find_rotation_angle_hough(input_image_file):
    # load image
    image = io.imread(input_image_file, as_grey=True)

    # binarize image with otsu
    thresh = threshold_otsu(image)
    image = image > thresh

    # apply sobel filter
    image = sobel(image)
    image = -image

    angle_rotation = objective_function_hough(image)
    print_hough_analysis(image, angle_rotation, input_image_file)

    print('======================================================================================')
    print('Input file:', input_image_file)
    print('Mode: Hough')
    print('Angle to rotate:', angle_rotation)
    print('======================================================================================')

    return angle_rotation


def save_image(filename, axis='off'):
    """    
    :param filename: 
    :param title: 
    :param axis: 
    :return: 
    """"""
    Saves to file whatever we have plotted to matplotlib so far
    :param filename: output file saved
    :param title: title of the plot
    :return: None
    """
    plt.axis(axis)
    plt.savefig(filename)
    plt.clf()


def main():
    """
    Usage: python3 alinhar.py imagem_entrada.png <h|p> imagem_saida.png
    """
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

