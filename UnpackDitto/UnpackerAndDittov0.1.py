# Unpack&Ditto 1.0 beta
# por Ygor Moreira Lima
# UFF - Universidade Federal Fluminense
# Graduacao em Sistemas de Informacao

import os
import subprocess
diretorio = input("Digite o diretorio dos arquivos: ")
extensao = input("Digite o tipo de arquivo. Ex: .zip, .rar: ")
comando = "ls " + diretorio
saida0 = subprocess.check_output(comando)
print(saida0)
os.system("echo 'testing!'")