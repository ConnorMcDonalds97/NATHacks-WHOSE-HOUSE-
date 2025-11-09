'''
TO BE INVOKED IN THE PYGAME SCRIPT!
'''
from song_processing import assign_data_to_keys
from song_processing import get_beats_json

def return_keys_assignments_and_populate_json(midifile, beat_type, num_sensors=4, instrument=-1, min_note_duration=0.2, max_simultaneous_notes=2, time_between_notes=2):
    '''
    Example:
    song_title = 'Never Gonna Give You Up' (or any string to be queried from the songs json)
    beat_type = 0 for tempo, 1 for melody
    num_sensors = 4 or the number of keys to be displayed on the screen
    instrument = -1 for detect the melody instrument, or specify an int [0,127]
    '''
    get_beats_json.return_beat_timestamps(midifile, beat_type, num_sensors, instrument, min_note_duration, max_simultaneous_notes, time_between_notes)
    return assign_data_to_keys.get_pitch_categories(beat_type, num_sensors)

if __name__ == '__main__':
    beats = return_keys_assignments_and_populate_json("Bohemian Rhapsody", beat_type=1, num_sensors=4, instrument=-1)
    for b in beats:
        print(b)
        print("\n")