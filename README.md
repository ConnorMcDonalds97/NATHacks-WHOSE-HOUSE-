# Inspiration
ReBeat drew inspiration from a study that concluded using musical instruments in motor therapy is an "innovative therapeutic strategy is an effective approach for motor skill neurorehabilitation." [1] Additionally, through experience with some team members own physical therapy, our team found that rehabilitation can be a tedious and unmotivating process. To overcome this and incorporate the effects of the study, sought to gamify the recovery process.

[1] Schneider S, Schönle PW, Altenmüller E, Münte TF. Using musical instruments to improve motor skill recovery following a stroke. J Neurol. 2007 Oct;254(10):1339-46. doi: 10.1007/s00415-006-0523-2. Epub 2007 Jan 27. PMID: 17260171.

# What it does
ReBeat is designed to help patients in all stages of their rehabilitation driven by the use of a glove equipped with flex sensors to track flexion and extension of their fingers. Linked with our rhythm game, patients move their fingers to the beat of audio and visual cues. The glove interprets the movement of the fingers and reflects in game. The gamification of the recovery process grants to the patient instant gratification and over time, demonstrates clear numerical growth through scores and adjustable thresholds for sensing finger movement.

# How we built it
Our project bridges Arduino hardware, Pygame software, and melody/rhythm processing.

We fit flex sensors onto a glove and use an Arduino to read real-time finger flexion and extension.
Our Python script uses multithreading to simultaneously run our Pygame game logic while updating the flex sensor feedback.
The melody, chords, and tempo are assigned by processing a Musical Instrument Digital Interface (MIDI) file and assigning melody pitches to the in-game tiles.
