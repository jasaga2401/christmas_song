

# play Christmas song
import pygame

def play_mp3(file_path):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load(file_path)

    # Play the music
    pygame.mixer.music.play()

    # Wait for the music to play before exiting
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

# Replace 'your_song.mp3' with the path to your mp3 file
play_mp3('jingle.mp3')



