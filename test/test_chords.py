import harmony


def test_get_chords():

    c = harmony.get_chords(harmony.modes.DORIAN,
                           harmony.keys.Key.D, seventh=True)[0]
    assert str(c[0]) == "Dm7"


test_get_chords()
