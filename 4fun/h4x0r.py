import os
import time

banner = """
$$\       $$\   $$\            $$$$$$\            
$$ |      $$ |  $$ |          $$$ __$$\           
$$$$$$$\  $$ |  $$ |$$\   $$\ $$$$\ $$ | $$$$$$\  
$$  __$$\ $$$$$$$$ |\$$\ $$  |$$\$$\$$ |$$  __$$\ 
$$ |  $$ |\_____$$ | \$$$$  / $$ \$$$$ |$$ |  \__|
$$ |  $$ |      $$ | $$  $$<  $$ |\$$$ |$$ |      
$$ |  $$ |      $$ |$$  /\$$\ \$$$$$$  /$$ |      
\__|  \__|      \__|\__/  \__| \______/ \__|      
@LittleBoy_BB
"""

haski_all_the_thinks = [
    'Iniciando sistemas...',
    'Otimizando sistema.....',
    'Carregando modulos CC+....',
    'Carregando plugins...',
    'Carregando configuracoes basicas e de plugins......',
    'Pegar o rexona...',
    'Assistir um video de haski no youtube..',
    'Baixar um haski.exe.....',
    'Pegar o ip do amiguinho.....',
    'Despistar o FBI',
    '   - Entrar no wifi haskiado do vizinho...',
    '   - Usar uma lista de proxy...',
    '   - Abrir o chrome em modo anonimato 100%...',
    'Carregando modulos das tecnicas Darlisson Araujo.......',
    'Aumentar poder de haskiagem para +8000'
    '\n',
    'INICIANDO HASKIAGEM............',
    '   - Engenharia psiquica [ON]',
    '   - Ameaca de DDoS',
    '   - Deface',
    '   - Baixar exploits',
    '   - Executar exploits 100000x',
    'MICROONDAS HASKIADO COM SUCESSO',
    'HP 9100 HASKIADA COM SUCESSO',
    'FARMACIA DA ESQUINA HASKIADA COM SUCESSO',
    'MATA AMAZONICA HASKIADA COM SUCESSO',
    'PORTA DE MADEIRA HASKIADA COM SUCESSO',
    'TIJOLO HASKIADO COM SUCESSO'
]
history = ''

for hackudo in haski_all_the_thinks:
    aa = ''
    for letter in hackudo:
        aa = aa + letter
        os.system('clear')
        print banner
        print history
        print "[*] " + aa
        time.sleep(0.1)

    history = history + "\n[+] " + hackudo
