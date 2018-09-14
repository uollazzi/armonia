from harmony import modes, keys
from harmony.logic import get_scale


def test_get_scale():

    s = get_scale(modes.DORIAN, keys.Key.D)

    assert str(s[0]) == "D"
