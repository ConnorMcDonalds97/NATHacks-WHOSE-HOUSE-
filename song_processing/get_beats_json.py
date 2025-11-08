
'''
Given a midi (.mid) file, get the:
- total length of the song in seconds
- melody or beat
- timestamps of the beats in seconds
-  
'''
import pygame

import mido

from midi2audio import FluidSynth

import requests
import os

import time
import json

import pretty_midi

NGGYU = "Never Gonna Give You Up"
BR = "Bohemian Rhapsody"

with open("../../song_processing/general_midi_instruments.json") as f:
    GM_PROGRAMS = json.load(f)

with open("../../song_processing/songs.json") as f:
    SONGS = json.load(f)


SAVE_WAV_TO_FOLDER = './'
BEATS_DATA_JSON = "../../song_processing/beats_data.json"

def midi_to_wav(midifile, wavfile, save_to_folder=SAVE_WAV_TO_FOLDER):
    fs= FluidSynth()
    fs.midi_to_audio(midifile, wavfile)

def get_midi_melody(midi_data, instrument_idx=-1):
    '''
    instrument_idx is -1 for using pretty midi to choose the most likely melody instrument, and in [0,127] if user manually chooses
    '''

    melody_instrument = None
    print(midi_data.instruments)
    if instrument_idx >= 0 and instrument_idx <= 127:
        matches = [inst for inst in midi_data.instruments if inst.program == instrument_idx]
        if matches:
            melody_instrument = matches[0]
        else:
            print("No instrument with that program found! Finding the most likely main melody...")

    if instrument_idx == -1 or melody_instrument==None:
        melody_instrument = max(
        [inst for inst in midi_data.instruments if not inst.is_drum],
        key=lambda inst: len(inst.notes)
        )
        print(f"Melody likely played by instrument program {melody_instrument.program}")
    
    melody_data = []
    for note in melody_instrument.notes:
        melody_data.append({
        "pitch": note.pitch,
        "start_time": note.start,
        "end_time": note.end,
        "duration": note.end - note.start
    })

    with open(BEATS_DATA_JSON, "w") as f:
        json.dump(melody_data, f, indent=2)

def get_midi_tempo(mididata):
    beats = mididata.get_beats().tolist()
    data = []
    duration = 0.2
    for beat in beats:
        data.append({
            "start_time": beat,
            "end_time": beat+duration,
            "duration": duration,
        })
    print(beats)
    with open(BEATS_DATA_JSON, "w") as f:
        json.dump(data, f, indent=2)
    return beats

def return_beat_timestamps(song_name, beat_type, num_sensors=4, instrument=-1):
    '''
    get either the bpm of the song or the beat type
    split the beats into num_sensors number of arrays, perhaps correlate to pitch?

    TODO: how many beats 
    '''
    midifile = SONGS[song_name]["title"]+'.mid'

    midi_data = pretty_midi.PrettyMIDI(midifile)
    match beat_type:
        case 'melody':
            get_midi_melody(midi_data=midi_data, instrument_idx=instrument) #writes to JSON
        case 'metronome':
            get_midi_tempo(mididata=midi_data)

if __name__ == "__main__":
    return_beat_timestamps(song_name= NGGYU, beat_type='melody', num_sensors=4, instrument=-1)