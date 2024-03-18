import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 300, 100
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Music Player")

music_files = ["music1.mp3", "music2.mp3", "music3.mp3"]
current_music_index = 0

def load_and_play_music():
    pygame.mixer.music.load(music_files[current_music_index])
    pygame.mixer.music.play(-1)  

running = True
playing = False  
load_and_play_music()  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif event.key == pygame.K_RIGHT:  
                current_music_index = (current_music_index + 1) % len(music_files)
                load_and_play_music()
                playing = True
            elif event.key == pygame.K_LEFT:  
                current_music_index = (current_music_index - 1) % len(music_files)
                load_and_play_music()
                playing = True

    window.fill((255, 255, 255))
    pygame.display.update()

pygame.quit()
