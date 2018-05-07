#!/usr/bin/env bash

python3 alinhar.py neg_4.png h hough_fixed_neg_4.png
python3 alinhar.py neg_28.png h hough_fixed_neg_28.png
python3 alinhar.py pos_24.png h hough_fixed_pos_24.png
python3 alinhar.py pos_41.png h hough_fixed_pos_41.png
python3 alinhar.py sample1.png h hough_fixed_sample1.png
python3 alinhar.py sample2.png h hough_fixed_sample2.png

python3 alinhar.py neg_4.png p projection_fixed_neg_4.png
python3 alinhar.py neg_28.png p projection_fixed_neg_28.png
python3 alinhar.py pos_24.png p projection_fixed_pos_24.png
python3 alinhar.py pos_41.png p projection_fixed_pos_41.png
python3 alinhar.py sample1.png p projection_fixed_sample1.png
python3 alinhar.py sample2.png p projection_fixed_sample2.png