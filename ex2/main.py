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







def main():
# imagem_entrada.png texto_entrada.txt plano_bits imagem_saida.png
    # read inputs
    input_image_file = sys.argv[0]
    message_file = sys.argv[1]
    bit_plane = sys.argv[2]
    output_image_file = sys.argv[3]

    bit_plane_file = 'bits.' + input_image_file
    message_string = read_file(message_file)

    write_message(input_image_file, coded_file, message_string, bit_plane)


    print_bit_planes(coded_file, bit_plane_file, bit_plane)


if __name__ == "__main__":
    main()
