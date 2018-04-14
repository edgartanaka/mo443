import math
import matplotlib
import sys
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, io

'''
Exercise: 2
Author: Edgar Tanaka
RA: 023577

MO443 - Image Processing
Prof. Helio Pedrini
State University of Campinas
1st semester 2018
'''


def get_bit(b, i):
    return (b >> i) & 1


def write_bit(_byte, bit, i):
    bit_index = 2 ** i
    if bit == 0:
        return (_byte & ~bit_index)
    else:
        return (_byte | bit_index)


def read_file(input_file):
    with open(input_file, 'r') as myfile:
        data = myfile.read().replace('\n', '')
        return data


def write_message(input_image_file, output_image_file, message, bit_plane=0):
    '''
    bit_plane: 0 is the least significant, 1 is the 2nd least significant and so on...
    '''
    img = io.imread(input_image_file)
    original_shape = img.shape
    img = img.flatten()
    message = message + '\0'
    ascii_bytes = [ord(c) for c in message]

    img_index = 0
    for message_index, ascii_byte in enumerate(ascii_bytes):
        for bit_index in range(7, -1, -1):
            bit = get_bit(ascii_byte, bit_index)

            img[img_index] = write_bit(img[img_index], bit, bit_plane)
            img_index += 1

    print("modified bits:", img_index)
    print("image shape:", original_shape)
    print("total pixels:", original_shape[0] * original_shape[1])
    print("len:", len(img))
    percentage_modified = (img_index)/len(img)
    pixels_modified = math.ceil(img_index/3)
    print("modified pixels:", pixels_modified)
    print("modified % pixels:", percentage_modified)

    io.imsave(output_image_file, img.reshape(original_shape))


def print_bit_planes(input_file, output_file, bit_plane=0):
    img = io.imread(input_file)
    mask = 2 ** bit_plane
    bit_plane_img = np.bitwise_and(img, mask)
    #print(bit_plane_img[:10][:10])
    io.imsave(output_file, bit_plane_img)


def main():
    # read inputs
    input_image_file = sys.argv[1]
    message_file = sys.argv[2]
    bit_plane = int(sys.argv[3])
    output_image_file = sys.argv[4]

    bit_plane_file = 'bits.' + input_image_file
    message_string = read_file(message_file)

    write_message(input_image_file, output_image_file, message_string, bit_plane)

    print_bit_planes(output_image_file, bit_plane_file, bit_plane)


if __name__ == "__main__":
    main()
