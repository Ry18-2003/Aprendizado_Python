# programa para executar um mp3

from pygame import init, mixer_music, quit

# inicia o pygame
init()

# Carrega a música indicada
mixer_music.load('C:/Users/Richard/Music/zelda.mp3')

# Inicia a música indicada
mixer_music.play(start=120.0)

# Faz o programa continuar rodando enquanto estiver tocando musica
while mixer_music.get_busy():
    continue
# Finaliza o pygame
quit()
