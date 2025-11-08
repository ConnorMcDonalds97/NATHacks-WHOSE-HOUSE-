'''
TO BE INVOKED IN THE PYGAME SCRIPT!
'''
import assign_data_to_keys
import get_beats_json

def return_keys_assignments_and_populate_json(song_title, beat_type, num_sensors=4, instrument=-1):
    '''
    Example:
    song_title = 'Never Gonna Give You Up' (or any string to be queried from the songs json)
    beat_type = 0 for tempo, 1 for melody
    num_sensors = 4 or the number of keys to be displayed on the screen
    instrument = -1 for detect the melody instrument, or specify an int [0,127]
    '''
    get_beats_json.return_beat_timestamps(song_title, beat_type, num_sensors, instrument)
    return assign_data_to_keys.get_pitch_categories(beat_type, num_sensors)