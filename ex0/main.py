'''
Exercicio 0
Disciplina: MO443 Processamento de Imagens
Professor: Helio Pedrini
1o. semestre de 2018

Aluno: Edgar Kenji Tanaka
RA: 023577
'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import misc

def get_histogram(img, out_file):
    # show histogram
    plt.hist(img.ravel().astype(int), 256, [0, 256])
    plt.title("Histograma da imagem: " + out_file)
    plt.savefig(out_file)
    plt.clf()


def print_stats(img, out_file):
    print('------------------------------------------')
    print("Estatisticas da imagem:", out_file)
    print("largura:", img.shape[0])
    print("altura:", img.shape[1])
    print("intensidade minima:", img.min())
    print("intensidade maxima:", img.max())
    print("intensidade media: %.2f" % img.mean())
    print('------------------------------------------\n')


def get_negative(img, out_file):
    # get negative of the image
    negative_img = 255 - img
    plt.imshow(negative_img, cmap='gray', vmin=0, vmax=255)
    plt.title("Negativo: " + out_file)
    plt.savefig(out_file)
    plt.clf()


def get_converted(img, out_file):
    # convert to gray intensity scale [120,180]
    # total range is 180 - 120 = 60
    # we'll use a simple rule of three
    converted_img = (img * (60/256)) + 120
    plt.imshow(converted_img, cmap='gray', vmin=0, vmax=255)
    plt.title("Transformacao de intensidade: " + out_file)
    plt.savefig(out_file)
    plt.clf()


def main():
    files = [
        'baboon.png',
        'butterfly.png',
        'city.png',
        'house.png',
        'seagull.png',
    ]

    print('------------- Pre-requirements -----------')
    print('The following files must be in the current directory:')
    print(', '.join(files))
    print('------------------------------------------\n')
    print('\n\n')

    for f in files:
        # open image file and stores it in a numpy array
        img = misc.imread(f)

        print_stats(img, f)
        get_histogram(img, 'histogram.' + f)
        get_negative(img, 'negative.' + f)
        get_converted(img, 'converted.' + f)


if __name__ == "__main__":
    main()
