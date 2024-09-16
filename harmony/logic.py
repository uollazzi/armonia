from .note_names import NOTES_SHARP, NOTES_FLAT
from pychord import find_chords_from_notes


def get_note_name(index, key):
    """ """
    note = key.value + index

    notes = []

    # TODO: sistema questa che fa schifo
    if str(key).lower().find("b") > -1:
        notes = NOTES_FLAT
    else:
        notes = NOTES_SHARP

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
        retval.append(get_note_name(i, key))

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

        retval.append(find_chords_from_notes(chord)[0])

    return retval
