'''
Given the beats_data.json and the number of keys specified by the user and the pitch,
sort the beats to different arrays corresponding to the keys

For instance, say we specify 4 'piano keys' and 'melody'. Then, find lowest pitch and highest pitch, divide into four pitch categories from lowest to highest,
so that each array (lowest, mid lowest, mid highest, highest) is populated with the timestamps of the pitches

'''
import json
import numpy as np
import random

def even_divisions(low, high, n):
    step = (high - low) / n
    return [low + i * step for i in range(n + 1)]

def get_pitch_categories(mode, n):
    '''
    Returns the pitch categories
    mode == 0: metronome
    mode == 1: melody
    '''
    with open("./song_processing/beats_data.json") as f:
        BEATS = json.load(f)

    beats_assignments = [] #assign the beats to the keys 
    for i in range(n):
        beats_assignments.append([]) #append n empty lists. idx 0 is lowest pitch, idx n-1 is highest
    
    if mode==1: #melody, sort by pitch
        pitches = [beat['pitch'] for beat in BEATS]
        lowest_pitch, highest_pitch = min(pitches), max(pitches)

        pitch_categories = even_divisions(lowest_pitch, highest_pitch, n)
        prevbeatidx=None
        for beat in BEATS[1:]:
            # put each beat['start_time'] with beat['duration'] into the correct category 
            p = beat['pitch']
            start = beat['start_time']
            dur = beat['duration']

            # find which bin pitch belongs to
            idx = np.digitize(p, pitch_categories) - 1
            idx = max(0, min(idx, n - 1))  # clamp to valid range
            
            if prevbeatidx is not None:
                if prevbeatidx == idx:
                    if prevbeatidx == n-1:
                        idx -=1
                    else:
                        idx+=1
            
            #just to make sure idx is always valid
            idx = max(0,idx)
            idx = min(idx,n-1)

            # append (time, duration, pitch)
            beats_assignments[idx].append({
                "start_time": start,
                "duration": dur,
                # "pitch": p
            })
            prevbeatidx = idx


    if mode ==0: #tempo, sort randomly!
        for beat in BEATS:
            idx=random.randint(0,n-1)
            beats_assignments[idx].append({
                "start_time": beat['start_time'],
                "duration": beat['duration'],
            })
    return beats_assignments


if __name__ == '__main__':
    beats_assignments = get_pitch_categories(1,4)
