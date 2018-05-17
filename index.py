import modes
import note_names

START_NOTE = 0
NOTES = note_names.NOTES_FLAT
MODE = modes.IONIAN

def get_note_name(index):
    if index > 12:
        index = index - 12
    return NOTES[index]

def get_note_index(mode, n):
    if n > 6:
        n = n - 6 * (int(n / 6) + 1)
    return mode[n]

# PRINT THE SCALE
for i in MODE:
    next_note = START_NOTE + i    
    print(get_note_name(next_note))


# PRINT THE CHORDS
for i in MODE:
    next_note = START_NOTE + i    

    chord = get_note_name(get_note_index(MODE, next_note)) + get_note_name(get_note_index(MODE, next_note + 2)) + get_note_name(get_note_index(MODE, next_note + 4))
    print(chord)


