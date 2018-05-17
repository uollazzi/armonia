import modes
import note_names

START_NOTE = 2
NOTES = note_names.NOTES_FLAT

# PRINT THE SCALE
print(NOTES[START_NOTE])
for i in modes.DORIAN:
    next_note = START_NOTE + i
    if next_note >= 12:
        next_note = next_note - 12
    print(NOTES[next_note])
