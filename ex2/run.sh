rm decoded.message*.txt
rm bits*.png
rm encoded*.png

python3 encode.py baboon.png message_small.txt 2 encoded.baboon.png
python3 encode.py monalisa.png message_small.txt 2 encoded.monalisa.png
python3 encode.py peppers.png message_small.txt 2 encoded.peppers.png
python3 encode.py watch.png message_small.txt 2 encoded.watch.png

python3 decode.py encoded.baboon.png 2 decoded.message.baboon.txt
python3 decode.py encoded.monalisa.png 2 decoded.message.monalisa.txt
python3 decode.py encoded.peppers.png 2 decoded.message.peppers.txt
python3 decode.py encoded.watch.png 2 decoded.message.watch.txt

