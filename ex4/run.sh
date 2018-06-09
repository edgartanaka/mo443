#!/usr/bin/env bash
#
# Usage: python3 main.py -m <method> -a <angle> -e <scale> -d <width> <height> -i <input image> -o <output image>
#

rm rotated*.png
rm resized*.png
rm scaled*.png

python3 main.py -m 1 -a 27 -i baboon.png -o rotated1_baboon.png
python3 main.py -m 1 -e 2.63 -i baboon.png -o scaled1_baboon.png
python3 main.py -m 1 -d 1000 500 -i baboon.png -o resized1_baboon.png
python3 main.py -m 1 -a 27 -i butterfly.png -o rotated1_butterfly.png
python3 main.py -m 1 -e 2.63 -i butterfly.png -o scaled1_butterfly.png
python3 main.py -m 1 -d 1000 500 -i butterfly.png -o resized1_butterfly.png
python3 main.py -m 1 -a 27 -i city.png -o rotated1_city.png
python3 main.py -m 1 -e 2.63 -i city.png -o scaled1_city.png
python3 main.py -m 1 -d 1000 500 -i city.png -o resized1_city.png
python3 main.py -m 1 -a 27 -i house.png -o rotated1_house.png
python3 main.py -m 1 -e 2.63 -i house.png -o scaled1_house.png
python3 main.py -m 1 -d 1000 500 -i house.png -o resized1_house.png
python3 main.py -m 1 -a 27 -i seagull.png -o rotated1_seagull.png
python3 main.py -m 1 -e 2.63 -i seagull.png -o scaled1_seagull.png
python3 main.py -m 1 -d 1000 500 -i seagull.png -o resized1_seagull.png
python3 main.py -m 2 -a 27 -i baboon.png -o rotated2_baboon.png
python3 main.py -m 2 -e 2.63 -i baboon.png -o scaled2_baboon.png
python3 main.py -m 2 -d 1000 500 -i baboon.png -o resized2_baboon.png
python3 main.py -m 2 -a 27 -i butterfly.png -o rotated2_butterfly.png
python3 main.py -m 2 -e 2.63 -i butterfly.png -o scaled2_butterfly.png
python3 main.py -m 2 -d 1000 500 -i butterfly.png -o resized2_butterfly.png
python3 main.py -m 2 -a 27 -i city.png -o rotated2_city.png
python3 main.py -m 2 -e 2.63 -i city.png -o scaled2_city.png
python3 main.py -m 2 -d 1000 500 -i city.png -o resized2_city.png
python3 main.py -m 2 -a 27 -i house.png -o rotated2_house.png
python3 main.py -m 2 -e 2.63 -i house.png -o scaled2_house.png
python3 main.py -m 2 -d 1000 500 -i house.png -o resized2_house.png
python3 main.py -m 2 -a 27 -i seagull.png -o rotated2_seagull.png
python3 main.py -m 2 -e 2.63 -i seagull.png -o scaled2_seagull.png
python3 main.py -m 2 -d 1000 500 -i seagull.png -o resized2_seagull.png
python3 main.py -m 3 -a 27 -i baboon.png -o rotated3_baboon.png
python3 main.py -m 3 -e 2.63 -i baboon.png -o scaled3_baboon.png
python3 main.py -m 3 -d 1000 500 -i baboon.png -o resized3_baboon.png
python3 main.py -m 3 -a 27 -i butterfly.png -o rotated3_butterfly.png
python3 main.py -m 3 -e 2.63 -i butterfly.png -o scaled3_butterfly.png
python3 main.py -m 3 -d 1000 500 -i butterfly.png -o resized3_butterfly.png
python3 main.py -m 3 -a 27 -i city.png -o rotated3_city.png
python3 main.py -m 3 -e 2.63 -i city.png -o scaled3_city.png
python3 main.py -m 3 -d 1000 500 -i city.png -o resized3_city.png
python3 main.py -m 3 -a 27 -i house.png -o rotated3_house.png
python3 main.py -m 3 -e 2.63 -i house.png -o scaled3_house.png
python3 main.py -m 3 -d 1000 500 -i house.png -o resized3_house.png
python3 main.py -m 3 -a 27 -i seagull.png -o rotated3_seagull.png
python3 main.py -m 3 -e 2.63 -i seagull.png -o scaled3_seagull.png
python3 main.py -m 3 -d 1000 500 -i seagull.png -o resized3_seagull.png
python3 main.py -m 4 -a 27 -i baboon.png -o rotated4_baboon.png
python3 main.py -m 4 -e 2.63 -i baboon.png -o scaled4_baboon.png
python3 main.py -m 4 -d 1000 500 -i baboon.png -o resized4_baboon.png
python3 main.py -m 4 -a 27 -i butterfly.png -o rotated4_butterfly.png
python3 main.py -m 4 -e 2.63 -i butterfly.png -o scaled4_butterfly.png
python3 main.py -m 4 -d 1000 500 -i butterfly.png -o resized4_butterfly.png
python3 main.py -m 4 -a 27 -i city.png -o rotated4_city.png
python3 main.py -m 4 -e 2.63 -i city.png -o scaled4_city.png
python3 main.py -m 4 -d 1000 500 -i city.png -o resized4_city.png
python3 main.py -m 4 -a 27 -i house.png -o rotated4_house.png
python3 main.py -m 4 -e 2.63 -i house.png -o scaled4_house.png
python3 main.py -m 4 -d 1000 500 -i house.png -o resized4_house.png
python3 main.py -m 4 -a 27 -i seagull.png -o rotated4_seagull.png
python3 main.py -m 4 -e 2.63 -i seagull.png -o scaled4_seagull.png
python3 main.py -m 4 -d 1000 500 -i seagull.png -o resized4_seagull.png

