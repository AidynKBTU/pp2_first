import pygame
import sys

pygame.init()

width, height = 400, 200
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")

music_list = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_song = 0
pygame.mixer.music.load(music_list[current_song])

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(music_list)
    pygame.mixer.music.load(music_list[current_song])
    pygame.mixer.music.play()

def previous_song():
    global current_song
    current_song = (current_song - 1) % len(music_list)
    pygame.mixer.music.load(music_list[current_song])
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    stop_music()
                else:
                    play_music()
            elif event.key == pygame.K_n: 
                next_song()
            elif event.key == pygame.K_p:
                previous_song()

pygame.quit()
sys.exit()
