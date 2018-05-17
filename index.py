NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

MAJOR = [2, 4, 5, 7, 9, 11]

START_NOTE = 2

print(NOTES[START_NOTE])
for i in MAJOR:
    next_note = START_NOTE + i
    if next_note >= len(NOTES):
        next_note = next_note - 12
    print(NOTES[next_note])
