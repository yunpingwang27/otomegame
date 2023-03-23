from vndb_thigh_highs.models import Flag, Release, AnimationType, ReleaseType
from test_case import CommandTest, ResponseTest

class GetReleaseCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(Release)

    def test_release_basic(self):
        expected = 'get release basic (id = 350)'
        text_command = self.command.make_command(Release.id == 350, Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_release_all_flags(self):
        expected = 'get release basic,details,lang,links,producers,vn (id = 350)'
        text_command = self.command.make_command(Release.id == 350)
        self.assertEqual(text_command, expected)

class GetReleaseResponseTest(ResponseTest):
    def test_release(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.release_350(),
        ])
        releases = self.vndb.get_release(Release.id == 350)
        self.assertEqual(len(releases), 1)
        release = releases[0]
        self.assertEqual(release.id, 350)
        self.assertEqual(release.title, "Fate/Stay Night - First Press Limited Edition")
        self.assertEqual(release.gtin, '4560158370012')
        self.assertEqual(release.animation.ero, AnimationType.NO_ANIMATION)
        self.assertEqual(release.vns[0].release_type, ReleaseType.COMPLETE)
        self.assertEqual(len(release.languages), 1)
        language = release.languages[0]
        self.assertEqual(language.language, "ja")
        self.assertEqual(language.title, "Fate/Stay Night - First Press Limited Edition")
        self.assertEqual(language.original_title, "Fate/stay night 初回限定版")
        self.assertFalse(language.machine_translation)
        self.assertTrue(language.main)
        self.assertGreater(len(release.links), 1)
        link_found = False
        for link in release.links:
            if link.label == "ErogameScape":
                self.assertEqual(link.url, "https://erogamescape.dyndns.org/~ap2/ero/toukei_kaiseki/game.php?game=3254")
                link_found = True
        self.assertTrue(link_found)

    def test_release_null_fields(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.release_1588(),
        ])
        releases = self.vndb.get_release(Release.id == 1588)
        self.assertEqual(len(releases), 1)
        release = releases[0]
        self.assertEqual(release.voiced, None)
        self.assertEqual(release.animation.ero, None)
