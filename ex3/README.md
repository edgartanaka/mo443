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

# Rodar programa
python3 code.py imagem_entrada.png texto_entrada.txt plano_bits imagem_saida.png
python3 decode.py imagem_saida.png plano_bits texto_saida.txt
```
onde:
- code.py: programa que oculta mensagem de texto na imagem.
- decode.py: programa que recupera mensagem de texto da imagem.
- imagem_entrada.png: imagem no formato PNG em que sera embutida a mensagem.  
- imagem_saida.png: imagem no formato PNG com mensagem embutida.
- texto_entrada.txt: arquivo-texto contendo mensagem a ser oculta.
- texto_saida.txt: arquivo-texto contendo mensagem recuperada.
- plano_bits: tres planos de bits menos significativos representados pelos valores 0, 1 ou 2.