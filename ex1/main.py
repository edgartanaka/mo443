import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from skimage import measure, io

'''
Exercise: 1
Author: Edgar Tanaka
RA: 023577

MO443 - Image Processing
Prof. Helio Pedrini
State University of Campinas
1st semester 2018
'''


def show_objects_properties(input_file):
    '''
    Detect objects and save an image with each object labeled with its index.
    Prints properties of each object.
    :param input_file:
    :return:
    '''
    img = io.imread(input_file, as_grey=True)

    # detect objects and extract their properties
    # background is 1 (white)
    props = measure.regionprops(measure.label(img, background=1))

    areas = []
    for i, prop in enumerate(props):
        print('regiao: {:d}\tperimetro: {:.0f}\tarea: {:.0f}\tcentroide: ({:.1f}, {:.1f})'
              .format(i, prop.perimeter, prop.area, prop.centroid[0], prop.centroid[1]))

        # write text label on image
        plt.text(prop.centroid[1]-7, prop.centroid[0]+7, str(i), fontsize=10, color='black')
        areas.append(prop.area)

    # show labeled objects
    plot_only_contours(input_file)
    save_image('regions.' + input_file, 'Regiões rotuladas: ' + input_file)

    # print object's areas stats
    areas = np.array(areas)
    count_objects_per_size = np.array([np.sum(areas < 1500),
                                       np.sum((areas >= 1500) & (areas < 3000)),
                                       np.sum(areas >= 3000)])
    print('----------------------------------------------')
    print("numero total de objetos:", len(props))
    print('numero de objetos pequenos:', count_objects_per_size[0])
    print('numero de objetos medios:', count_objects_per_size[1])
    print('numero de objetos grandes:', count_objects_per_size[2])

    # plot histogram of objects per size
    fig, ax = plt.subplots()
    ind = np.arange(1,4)
    ax.set_xticklabels(['Pequeno', 'Medio', 'Grande'])
    ax.set_xticks(ind)
    plt.bar(ind, count_objects_per_size)

    # save image
    plt.ylabel('Contagem')
    save_image('hist.' + input_file, 'Histograma de áreas: ' + input_file, axis='on')


def plot_only_contours(input_file):
    '''
    Plots only the contours of the objects detected.
    :param input_file: file name of image containing objects and a white background
    :return: None. But plots in the current matplotlib
    '''
    img = io.imread(input_file, as_grey=True)
    contours = measure.find_contours(img, level=0.5)

    # start with blank image
    img = np.full(img.shape, 1)
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)

    # fill with the contour pixels in red
    for n, contour in enumerate(contours):
        plt.plot(contour[:, 1], contour[:, 0], 'red', linewidth=1)


def show_contours(input_file):
    '''
    Saves and image containing only the contours of the objects detected
    :param input_file: file name of image containing objects and a white background
    :return: None. Saves image with prefix "contours" in the current directory
    '''
    plot_only_contours(input_file)
    save_image('contours.' + input_file, ('Contornos: ' + input_file))


def show_grayscale(input_file):
    '''
    Saves the input_file image converted to grayscale
    :param input_file: colored image file name
    :return: None. Saves image with prefix "gray" in the current directory
    '''
    # read as gray and print it
    img = io.imread(input_file, as_grey=True)
    plt.imshow(img,  cmap='gray')
    save_image('gray.' + input_file, 'Escala de cinza: ' + input_file)


def save_image(filename, title, axis='off'):
    '''
    Saves to file whatever we have plotted to matplotlib so far
    :param filename:
    :param title:
    :return:
    '''
    plt.axis(axis)
    plt.title(title)

    plt.savefig(filename)
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
        show_objects_properties(f)

if __name__ == "__main__":
    main()
