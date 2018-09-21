from harmony import modes, keys, get_chords, get_scale
import random

# specifica la tonalità di partenza
key = keys.Key.E

# percentuale di cambio modo
mode_change_chance = 0.1

# modo casuale iniziale e suoi accordi
mode = random.choice(modes)
chords = get_chords(mode.intervals, key)

print(mode.name)

# grado I
current_chord = chords[0][0]
print(current_chord.chord)

for i in range(5):
    if random.random() < mode_change_chance and i > 2:
        mode = random.choice(modes)

        print(mode.name)
        chords = get_chords(mode.intervals, key)

    current_chord = random.choice(chords)[0]
    print(current_chord.chord)
