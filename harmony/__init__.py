import .modes
import .note_names
import .keys
from pychord import note_to_chord


def get_note_name(index, key):
    """

    """
    note = key.value + index

    notes = []

    # TODO: sistema questa che fa schifo
    if str(key).lower().find("b") > -1:
        notes = note_names.NOTES_FLAT
    else:
        notes = note_names.NOTES_SHARP

    if note > 11:
        note = note - 12
    return notes[note]


def get_note_by_index(mode, n):
    if n > 6:
        # gestisce le ottave
        n = n - 7
    return mode[n]


def get_scale(mode, key):
    retval = []

    # PRINT THE SCALE
    for i in mode:
        next_note = key.value + i

        retval.append(get_note_name(next_note, key))

    return retval


def get_chords(mode, key, seventh=False, ninth=False):
    retval = []
    # PRINT THE CHORDS
    for i in range(7):
        chord = []
        chord.append(get_note_name(get_note_by_index(mode, i), key))
        chord.append(get_note_name(get_note_by_index(mode, i + 2), key))
        chord.append(get_note_name(get_note_by_index(mode, i + 4), key))

        # settima
        if seventh:
            chord.append(get_note_name(get_note_by_index(mode, i + 6), key))

        # nona
        if ninth:
            chord.append(get_note_name(get_note_by_index(mode, i + 1), key))

        retval.append(note_to_chord(chord))

    return retval
