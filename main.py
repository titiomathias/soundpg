import pygame
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Soundboard")

sounds = {
    pygame.K_KP1: "audiolib/pistol-shot.mp3",
    pygame.K_KP2: "audiolib/fire.mp3",
    pygame.K_KP3: "audiolib/murmur_on_ferry.mp3",
    pygame.K_KP4: "audiolib/murmur-horror.mp3",
}

loaded_sounds = {}
for key, sound_file in sounds.items():
    try:
        loaded_sounds[key] = pygame.mixer.Sound(sound_file)
    except pygame.error as e:
        print(f"Erro ao carregar {sound_file}: {e}")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key in loaded_sounds:
                pygame.mixer.music.stop()
                loaded_sounds[event.key].play()
                print(f"Tocando: {sounds[event.key]}")
            elif event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()