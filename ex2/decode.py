import sys
import matplotlib

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


def read_message(input_file, bit_plane=0):
    img = io.imread(input_file).flatten()
    decoded_message = ''
    char_byte = 0

    for img_index, cell in enumerate(img):
        bit_index = 7 - (img_index % 8)

        # get bit where message is hidden
        bit = get_bit(cell, bit_plane)

        # compose char byte
        char_byte = char_byte | (bit << bit_index)

        # completed one char
        if bit_index == 0 and img_index > 0:
            if char_byte == 0:
                break  # end of message
            else:
                decoded_message += chr(char_byte)
                char_byte = 0  # reset

    return decoded_message


def write_file(message, output_file):
    with open(output_file, "w") as f:
        f.write(message)


def main():
    #
    # Usage:
    # python3 decode.py imagem_saida.png plano_bits texto_saida.txt
    #

    # read inputs
    coded_file = sys.argv[1]
    decoded_message_file = sys.argv[3]
    bit_plane = int(sys.argv[2])

    print('---------------------------------------------')
    print("Decoding image:", coded_file)
    decoded_message = read_message(coded_file, bit_plane)
    write_file(decoded_message, decoded_message_file)
    print("Decoded message to", decoded_message_file)
    print('---------------------------------------------')

if __name__ == "__main__":
    main()


