# executar um arquivo mp3

from pygame import init, mixer_music, quit

# Inicia o pygame
init()

# Carrega o arquivo MP3
mixer_music.load("C:/Users/Richard/Music/zelda.mp3")

# Reproduz o arquivo MP3
mixer_music.play(loops=0, start=0.0)

# Mantém o programa em execução
while mixer_music.get_busy():
    continue

# Encerrar o pygame
quit()
