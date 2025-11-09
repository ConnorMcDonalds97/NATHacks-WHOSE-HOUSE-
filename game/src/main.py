import pygame
import const

from game import Game

from midi2audio import FluidSynth
import json

with open("./song_processing/general_midi_instruments.json") as f:
    GM_PROGRAMS = json.load(f)

with open("./song_processing/songs.json") as f:
    SONGS = json.load(f)

SONG="Never Gonna Give You Up"
beat_type=1 
num_sensors=4 
instrument=-1 
min_note_duration=0.2
max_sim_notes=2 
time_bn_notes=1.

WAVFILE = SONGS[SONG]["title"]+'.wav'
MIDFILE = SONGS[SONG]["title"]+'.mid'
with open(WAVFILE, "w") as f:
    pass



def main():
    pygame.init()
    
    running = True
    
    fs= FluidSynth()
    fs.midi_to_audio(MIDFILE, WAVFILE)


    # Load the WAV file
    pygame.mixer.music.load(WAVFILE) 


    game = Game(pygame.display.set_mode((const.SCREEN_WIDTH, const.SCREEN_HEIGHT)), SONG, beat_type, num_sensors, instrument, min_note_duration, max_sim_notes, time_bn_notes)
    game.draw()

    pygame.mixer.music.play(0,0.0)

    clock = pygame.time.Clock()

    dt = 0
    timer = 0
    while running:
        game.draw()

        dt = clock.tick(60)/1000.0

        timer += dt
        
        game.updateTiles(dt)
        
        #check if tile is below sensor -> if it is then increment front
        f1 = game.tiles1
        if (f1.front <  f1.len) and f1.data[f1.front].pos[1] > const.SCREEN_HEIGHT:
            if not f1.data[f1.front].checkHit():
                game.multiplier = 1
            f1.front += 1
        f2 = game.tiles2
        if (f2.front <  f2.len) and f2.data[f2.front].pos[1] > const.SCREEN_HEIGHT:
            if not f2.data[f2.front].checkHit():
                game.multiplier = 1
            f2.front += 1
        f3 = game.tiles3
        if (f3.front <  f3.len) and f3.data[f3.front].pos[1] > const.SCREEN_HEIGHT:
            if not f3.data[f3.front].checkHit():
                game.multiplier = 1
            f3.front += 1
        f4 = game.tiles4
        if (f4.front <  f4.len) and f4.data[f4.front].pos[1] > const.SCREEN_HEIGHT:
            if not f4.data[f4.front].checkHit():
                game.multiplier = 1
            f4.front += 1

        print(game.multiplier)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game.sensor1.setColour(const.WHITE)
                    game.checkSensor(1)
                if event.key == pygame.K_2:
                    game.sensor2.setColour(const.WHITE)
                    game.checkSensor(2)
                if event.key == pygame.K_3:
                    game.sensor3.setColour(const.WHITE)
                    game.checkSensor(3)
                if event.key == pygame.K_4:
                    game.sensor4.setColour(const.WHITE)
                    game.checkSensor(4)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_1:
                    game.sensor1.setColour(const.RED)
                if event.key == pygame.K_2:
                    game.sensor2.setColour(const.GREEN)
                if event.key == pygame.K_3:
                    game.sensor3.setColour(const.ORANGE)
                if event.key == pygame.K_4:
                    game.sensor4.setColour(const.BLUE)

        pygame.display.update()

    pygame.quit()

main()