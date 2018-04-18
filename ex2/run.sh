# Resetting
rm decoded*.txt
rm bits*.png
rm encoded*.png
rm channel*.png

# Encoding
echo "Encoding..."
python3 encode.py baboon.png message_big.txt 0 encoded0.baboon.png
python3 encode.py monalisa.png message_small.txt 1 encoded1.monalisa.png
python3 encode.py peppers.png message_big.txt 2 encoded2.peppers.png
python3 encode.py watch.png message_too_big.txt 2 encoded2.watch.png

# Decoding
echo "\n\nDecoding..."
python3 decode.py encoded0.baboon.png 0 decoded0.baboon.txt
python3 decode.py encoded1.monalisa.png 1 decoded1.monalisa.txt
python3 decode.py encoded2.peppers.png 2 decoded2.peppers.txt
python3 decode.py encoded2.watch.png 2 decoded2.watch.txt


