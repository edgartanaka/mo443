# Ambiente testado
- Ubuntu 16.04.4 LTS
- virtualenv (para isolar um ambiente de execução)
- pip (para instalação dos pacotes python)
- Python 3.5.2

# Como executar
A execução do programa é feita de forma simples. Basta rodar os comandos a seguir:
```
# Criar uma virtualenv isolada
$ virtualenv -p python3 venv
$ source venv/bin/activate

# Instalar bibliotecas python no ambiente
$ pip install -r requirements.txt

# Rodar programa
$ python3 main.py
```
