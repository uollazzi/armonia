class Mode:
    def __init__(self, name, intervals):
        self.name = name
        self.intervals = intervals


IONIAN = Mode('Ionian', [0, 2, 4, 5, 7, 9, 11])
DORIAN = Mode('Dorian', [0, 2, 3, 5, 7, 9, 10])
PHRYGIAN = Mode('Phrygian', [0, 1, 3, 5, 7, 8, 10])
LYDIAN = Mode('Lydian', [0, 2, 4, 6, 7, 9, 11])
MIXOLYDIAN = Mode('Mixolydian', [0, 2, 4, 5, 7, 9, 10])
AEOLIAN = Mode('Aeolian', [0, 2, 3, 5, 7, 8, 10])
LOCRIAN = Mode('Locrian', [0, 1, 3, 5, 6, 8, 10])


modes = [
    IONIAN,
    DORIAN,
    PHRYGIAN,
    LYDIAN,
    MIXOLYDIAN,
    AEOLIAN,
    LOCRIAN
]
