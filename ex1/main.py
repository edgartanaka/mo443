import matplotlib
matplotlib.use('Agg')
import skimage.io
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure

'''
Exercise: 1
Author: Edgar Tanaka
RA: 023577

MO443 - Image Processing
Prof. Helio Pedrini
State University of Campinas
1st semester 2018
'''

def get_props(input_file):
    img = skimage.io.imread(input_file, as_grey=True)
    props = measure.regionprops(measure.label(img, background=255))

    # label 1 is the background so we skip it
    props = props[1:]
    print("numero de regioes:", len(props))

    areas = []
    for i, prop in enumerate(props):
        # print properties of each region
        print('regiao: {:d}\tperimetro: {:.0f}\tarea: {:.0f}\tcentroide: ({:.1f}, {:.1f})'.format(i, prop.perimeter, prop.area, prop.centroid[0], prop.centroid[1]))

        # write text label on image
        plt.text(prop.centroid[1]-4, prop.centroid[0]+4, str(i), fontsize=10, color='red')
        areas.append(prop.area)

    # show labeled regions
    plt.imshow(img, cmap='gray')
    plt.title('Regiões rotuladas: ' + input_file)
    plt.savefig('regions.' + input_file)
    plt.clf()

    # print object's areas stats
    areas = np.array(areas)
    print('numero de regioes pequenas:', np.sum(areas < 1500))
    print('numero de regioes medias:', np.sum((areas >= 1500) & (areas < 3000)))
    print('numero de regioes grandes:', np.sum(areas >= 3000))

    # show histogram of areas
    plt.hist(areas, bins=[0, 1500, 3000, np.inf])
    plt.xlabel('Área')
    plt.ylabel('Número de regiões')
    plt.title('Histograma de áreas: ' + input_file)
    plt.savefig('hist.' + input_file)
    plt.clf()


def show_contours(input_file):
    img = skimage.io.imread(input_file, as_grey=True)
    contours = measure.find_contours(img, level=0.5)

    # start with blank image
    img = np.full(img.shape, 255)
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

    # fill with the contour pixels in red
    for n, contour in enumerate(contours):
        plt.plot(contour[:, 1], contour[:, 0], 'red', linewidth=1)

    # print image containing only the contours in red
    plt.title('Contornos: ' + input_file)
    plt.savefig('contours.' + input_file)
    plt.clf()


def show_grayscale(input_file):
    # read as gray and print it
    img = skimage.io.imread(input_file, as_grey=True)
    plt.imshow(img,  cmap='gray')
    plt.title('Escala de cinza: ' + input_file)
    plt.savefig('gray.' + input_file)
    plt.clf()


def main():
    files = [
        'objetos1.png',
        'objetos2.png'
    ]

    for f in files:
        print('\n\n------------------------------------------')
        print('Processing file:', f)
        print('------------------------------------------')
        show_grayscale(f)
        show_contours(f)
        get_props(f)

if __name__ == "__main__":
    main()
