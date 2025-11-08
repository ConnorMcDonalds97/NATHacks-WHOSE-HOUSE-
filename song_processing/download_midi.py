
'''
Download a midi file via requests 
'''
import pygame

import mido

from midi2audio import FluidSynth

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")

songfile = '/home/oliveoil/Desktop/NATHacks-WHOSE-HOUSE-/song_processing/Queen - Bohemian Rhapsody'
# print(mido.get_output_names())

# port = mido.open_output('Midi Through:Midi Through Port-0 14:0')

# mid=mido.MidiFile(midifile)
# for msg in mid.play():
#     port.send(msg)


# print("Playback finished.")

# # Close the port when done
# port.close()

fs= FluidSynth()
fs.midi_to_audio(songfile+'.mid', songfile+'.wav')


# Load the WAV file
pygame.mixer.music.load(songfile+".wav") 

# Play the music:
# -1 for continuous looping, 0 for single play
# 0.0 for starting at the beginning
pygame.mixer.music.play(-1, 0.0) 

# Keep the program running to allow music to play
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()