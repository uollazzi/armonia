import modes
import note_names
from pychord import note_to_chord

START_NOTE = 0
NOTES = note_names.NOTES_FLAT
MODE = modes.IONIAN

def get_note_name(index):
    note = START_NOTE + index    
    if note > 11:
        note = note - 12
    return NOTES[note]

def get_note_index(mode, n):
    if n > 6:       
        # gestisce le ottave
        n = n - 7        
    return mode[n]

# PRINT THE SCALE
for i in MODE:
    next_note = START_NOTE + i    
    # print(get_note_name(next_note))


# PRINT THE CHORDS
for i in range(7):
    next_note = MODE[i]     
    chord =[]
    chord.append(get_note_name(get_note_index(MODE, i)))
    chord.append(get_note_name(get_note_index(MODE, i + 2)))
    chord.append(get_note_name(get_note_index(MODE, i + 4)))
    # settime   
    chord.append(get_note_name(get_note_index(MODE, i + 6)))
    print(chord)
    print(note_to_chord(chord))


