
'''
Download a midi file via requests 
'''
import pygame

import mido

from midi2audio import FluidSynth

import requests
import os

import time

import pretty_midi

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()

download_midi_url = 'https://bitmidi.com/'

def download_midi(url, save_dir='midi_files'):
    os.makedirs(save_dir, exist_ok=True)
    

songfile = '/home/oliveoil/Desktop/NATHacks-WHOSE-HOUSE-/song_processing/Queen - Bohemian Rhapsody'
# print(mido.get_output_names())

# port = mido.open_output('Midi Through:Midi Through Port-0 14:0')

# mid=mido.MidiFile(midifile)
# for msg in mid.play():
#     port.send(msg)


# print("Playback finished.")

# # Close the port when done
# port.close()
# --- STEP 2: Extract melody timing from MIDI ---
midi_data = pretty_midi.PrettyMIDI(songfile+'.mid')
# Pick the non-drum instrument with most notes = likely melody
melody_inst = max(
    [i for i in midi_data.instruments if not i.is_drum],
    key=lambda inst: len(inst.notes)
)
melody_times = [note.start for note in melody_inst.notes]
melody_times.sort()

print(f"Found {len(melody_times)} melody notes.")
###



fs= FluidSynth()
fs.midi_to_audio(songfile+'.mid', songfile+'.wav')


# Load the WAV file
pygame.mixer.music.load(songfile+".wav") 

# Play the music:
# -1 for continuous looping, 0 for single play
# 0.0 for starting at the beginning
pygame.mixer.music.play(-1, 0.0) 
start_time = time.time()
mel_idx=0
# Keep the program running to allow music to play
running = True
while running:
    now=time.time()-start_time
    if mel_idx < len(melody_times) and now >= melody_times[mel_idx]:
        
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)

pygame.quit()