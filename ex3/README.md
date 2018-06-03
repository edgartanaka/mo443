# Autor
Edgar Tanaka <edgartanaka@gmail.com>

# Ambiente testado

- Ubuntu 16.04.4 LTS
- virtualenv (para isolar um ambiente de execução)
- pip (para instalação dos pacotes python)
- Python 3.5.2
- tesseract-ocr

# Como executar

A execução do programa é feita de forma simples. Basta rodar os comandos a seguir:
```
# Instalar tesseract
apt-get install tesseract-ocr

# Criar uma virtualenv isolada
$ virtualenv -p python3 venv
$ source venv/bin/activate

# Instalar bibliotecas python no ambiente
$ pip install -r requirements.txt

# Rodar programa com técnica baseada em Hough
python3 alinhar.py input_image h output_image

# Rodar programa com técnica baseada em Projeção Horizontal
python3 alinhar.py input_image p output_image
```
