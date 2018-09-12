import modes
import keys
import __index__

for chord in __index__.get_chords(modes.DORIAN, keys.Key.D, seventh=True):
    print(chord)