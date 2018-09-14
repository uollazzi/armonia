from harmony import modes, keys
from harmony.logic import get_chords


def test_get_chords():

    c = get_chords(modes.DORIAN,
                   keys.Key.D, seventh=True)[0]
    assert str(c[0]) == "Dm7"
