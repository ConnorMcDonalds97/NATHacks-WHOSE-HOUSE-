
'''
Given a midi (.mid) file, get the:
- total length of the song in seconds
- melody or beat
- timestamps of the beats in seconds
-  
'''

import json

import pretty_midi


with open("./song_processing/general_midi_instruments.json") as f:
    GM_PROGRAMS = json.load(f)

BEATS_DATA_JSON = "./song_processing/beats_data.json"

def get_melody_instrument(midi_data_instruments):
    '''
    return: midi_data_instrument
    '''
    THRESHOLD = 2
    
    ret_inst = midi_data_instruments[0]
    maxCount = 0
    
    for inst in midi_data_instruments:
        count = 0
        notes = inst.notes
        length = len(notes)
        for i in range(length):
            if (i + 1 < length) and abs(notes[i].start - notes[i+1].start) < THRESHOLD:
                continue
            count += 1
            
        if count > maxCount:
            maxCount = count
            ret_inst = inst
    return ret_inst


def get_midi_melody(midi_data, instrument_idx=-1, min_note_duration = 0.1, max_simultaneous_notes = 2, time_between_notes = 1.0):
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
        for inst in midi_data.instruments:
            print(inst.notes)

        melody_instrument = get_melody_instrument(midi_data.instruments)
        '''
        
        '''
        print(f"Melody likely played by instrument program {melody_instrument.program}")
    
    
    notes = sorted(melody_instrument.notes, key=lambda n: n.start)

    # filter OUT short notes
    notes = [n for n in notes if n.end - n.start >= min_note_duration]

    simplified_notes=[]

    active_notes=[]
    time_since_last_note=0
    note=notes[0]
    simplified_notes.append(note)
    prevnote=note

    notes= notes[1:]
    for note in notes:
        time_since_last_note=note.start - prevnote.start
        if time_since_last_note > 0 and time_since_last_note < time_between_notes:
            pass
        else:
            active_notes = [ n for n in active_notes if n.end > note.start]
            active_notes.append(note)
            # if too many notes overlap, choose highest pitch
            if len(active_notes) > max_simultaneous_notes:
                # sort by pitch (highest-first for melody)
                active_notes = sorted(active_notes, key=lambda n: n.pitch, reverse=True)[:max_simultaneous_notes] # lambda to sort by pitch

            if note in active_notes:
                simplified_notes.append(note)

            # perhaps also a var to indicate the time since the most recent
            # have some amount of time between notes (simultaneous is OK)
            prevnote = note
        
    melody_data = []
    for note in simplified_notes:
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

def return_beat_timestamps(midifile, beat_type, num_sensors=4, instrument=-1, min_note_duration = 0.1, max_simultaneous_notes = 2, time_between_notes = 1.0):
    '''
    get either the bpm of the song or the beat type
    split the beats into num_sensors number of arrays, perhaps correlate to pitch?

    TODO: how many beats 
    '''

    midi_data = pretty_midi.PrettyMIDI(midifile)
    match beat_type:
        case 1: #melody
            get_midi_melody(midi_data=midi_data, instrument_idx=instrument, min_note_duration=min_note_duration, max_simultaneous_notes=max_simultaneous_notes, time_between_notes=time_between_notes) #writes to JSON
        case 0: #tempo
            get_midi_tempo(mididata=midi_data)

if __name__ == "__main__":
    midifile='./midi_songs/Never-Gonna-Give-You-Up-3.mid'
    midi_data = pretty_midi.PrettyMIDI(midifile)
    print(get_melody_instrument(midi_data.instruments))
    print(max(
        [inst for inst in midi_data.instruments if not inst.is_drum],
        key=lambda inst: len(inst.notes)
        ))
    # return_beat_timestamps(midifile='./midi_songs/Guns n Roses - Sweet Child O Mine.mid', beat_type=1, num_sensors=4, instrument=-1, min_note_duration = 0.1, max_simultaneous_notes = 2, time_between_notes = 3.0)
