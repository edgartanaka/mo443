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

def transform1(input_file):
    '''
    Ler e exibir uma imagem colorida formada por um conjunto de objetos distribu ́ıdos em um fundo
    branco. A imagem colorida deve ser convertida para nıveis de cinza.

    Transformar de colorido para preto e branco
    Mantém apenas os pixels brancos (255,255,255) e o resto converte
    para preto (0,0,0)
    '''
    # more manual way
    # img = skimage.io.imread(input_file)
    # img[(img[:,:,0] < 255) | (img[:,:,1] < 255) | (img[:,:,2] < 255)] = 0
    # skimage.io.imsave('transform1.' + input_file, img)

    # read image as gray scale and save it as transform1.***.png
    img = skimage.io.imread(input_file, as_grey=True)
    skimage.io.imsave('transform1.' + input_file, img)


def transform2(input_file):
    '''
    Apresentar os contornos (bordas) dos objetos presentes na imagem.
    '''
    # read as grayscale
    img = skimage.io.imread(input_file, as_grey=True)
    contours = measure.find_contours(img, 0.5)
    for n, contour in enumerate(contours):
        red_contours = np.zeros(img.shape)
        red_contours[contour[:, 1], contour[:, 0]] = 0
    skimage.io.imsave('transform2.' + input_file, red_contours)
    #
    # print(len(contours))
    # print(contours[0].shape)
    # skimage.io.imsave('countour0.png', contours[0])
    #
    #
    # skimage.io.imsave('transform2.' + input_file, img)



    # import numpy as np
    # import matplotlib.pyplot as plt
    #
    # from skimage import measure
    #
    # # Find contours at a constant value of 0.8
    # contours = measure.find_contours(img, 0.8)
    #
    # # Display the image and plot all contours found
    # fig, ax = plt.subplots()
    # ax.imshow(img, interpolation='nearest', cmap=plt.cm.gray)
    #
    # for n, contour in enumerate(contours):
    #     ax.plot(contour[:, 1], contour[:, 0], linewidth=2)
    #
    # ax.axis('image')
    # ax.set_xticks([])
    # ax.set_yticks([])
    # plt.show()

    pass

def transform3(input_file):
    '''
    Extrair as seguintes propriedades dos objetos: centroide, per ́ımetro e area.
    Para cada regiao (objeto), listar o perımetro e a area.
    '''
    pass

def get_histogram(input_file):

    pass

def main():
    files = ['objetos1.png', 'objetos2.png']
    for f in files:
        transform1(f)
        transform2(f)
        transform3(f)
        get_histogram(f)


main()
