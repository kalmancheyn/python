from unittest import TestCase
from removeaccent import removeAccentWithReplace, removeAccentWithDict

TEXT1 = """
A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre.
""".strip()


TEXT2 = """
A katalan zaszlo, a Senyera szineit fogja viselni a kovetkezo ideny soran a spanyol elvonalban szereplo FC Barcelona labdarugocsapata.

A Marca cimu sportnapilap hetfoi internetes kiadasa szerint az egyuttes jatekosai az idegenbeli merkozeseken huzzak majd magukra a sarga-piros csikozasu mezt - elso izben a klub tortenelme soran.

A dontes varhatoan nem marad politikai visszhang nelkul Spanyolorszagban, tekintettel a katalan onallosodasi torekvesekre.
""".strip()


class Test(TestCase):
    def test_remove_accent_with_replace(self):
        assert removeAccentWithReplace(TEXT1) == TEXT2

    def test_remove_accent_with_dict(self):
        assert removeAccentWithDict(TEXT1) == TEXT2

