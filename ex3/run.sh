#!/usr/bin/env bash
#
# Usage: python3 alinhar.py imagem_entrada.png <h|p> imagem_saida.png
#

# Hough
python3 alinhar.py neg_4.png h hough_fixed_neg_4.png
python3 alinhar.py neg_28.png h hough_fixed_neg_28.png
python3 alinhar.py pos_24.png h hough_fixed_pos_24.png
python3 alinhar.py pos_41.png h hough_fixed_pos_41.png
python3 alinhar.py sample1.png h hough_fixed_sample1.png
python3 alinhar.py sample2.png h hough_fixed_sample2.png
python3 alinhar.py smartphone.png h hough.fixed.smartphone.png
python3 alinhar.py smartphone2.png h hough.fixed.smartphone2.png
python3 alinhar.py smartphone3.png h hough.fixed.smartphone3.png
python3 alinhar.py revista.png h hough.fixed.revista.png

# Horizontal Projection
python3 alinhar.py neg_4.png p projection_fixed_neg_4.png
python3 alinhar.py neg_28.png p projection_fixed_neg_28.png
python3 alinhar.py pos_24.png p projection_fixed_pos_24.png
python3 alinhar.py pos_41.png p projection_fixed_pos_41.png
python3 alinhar.py sample1.png p projection_fixed_sample1.png
python3 alinhar.py sample2.png p projection_fixed_sample2.png
python3 alinhar.py smartphone.png p projection.fixed.smartphone.png
python3 alinhar.py smartphone2.png p projection.fixed.smartphone2.png
python3 alinhar.py smartphone3.png p projection.fixed.smartphone3.png
python3 alinhar.py revista.png p projection.fixed.revista.png

# OCR: before fixing text orientation
tesseract neg_4.png stdout
tesseract neg_28.png stdout
tesseract pos_24.png stdout
tesseract pos_41.png stdout
tesseract sample1.png stdout
tesseract sample2.png stdout


# OCR: after fixing text orientation
tesseract hough_fixed_neg_4.png  stdout
tesseract hough_fixed_neg_28.png stdout
tesseract hough_fixed_pos_24.png stdout
tesseract hough_fixed_pos_41.png stdout
tesseract hough_fixed_sample1.png stdout
tesseract hough_fixed_sample2.png stdout