from pygame import mixer 
from os import system
from time import sleep

mixer.init()
mixer.music.load('/home/parsival/Documentos/Curso de Python /musicas/m4.mp3')
mixer.music.play()

while True:
    system('clear')
    print('=='*10)
    print('Reproduzindo.')
    print('=='*10)
    sleep(1)
    system('clear')
    print('=='*10)
    print("Reproduzindo..")
    print('=='*10)
    sleep(1)
    system('clear')
    print('=='*10)
    print('Reproduzindo...')
    print('=='*10)
    sleep(1)
    system('clear')
    print('=='*10)
    print('Reproduzindo....')
    print('=='*10)
    sleep(1)
 
    
