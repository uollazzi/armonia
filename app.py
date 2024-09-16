from harmony import keys, get_chords, modes

key = keys.Key.G

print(f"            1     2     3     4     5     6     7")
for mode in modes:

    chords = [str(chord).ljust(5) for chord in get_chords(mode.intervals, key)]
    print((mode.name + ":").rjust(11), *chords)
