from vndb_thigh_highs.models import Flag, VN, User
from vndb_thigh_highs.error import TableUsedError
from test_case import CommandTest, ResponseTest

class GetVNCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(VN)

    def test_vn_basic(self):
        expected = 'get vn basic (id = 17)'
        text_command = self.command.make_command(VN.id == 17, Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_vn_all_flags(self):
        expected = 'get vn anime,basic,details,relations,screens,staff,stats,tags,titles (id = 17)'
        text_command = self.command.make_command(VN.id == 17)
        self.assertEqual(text_command, expected)

class GetVNResponseTest(ResponseTest):
    def test_vn(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.vn_17(),
        ])
        vns = self.vndb.get_vn(VN.id == 17)
        self.assertEqual(len(vns), 1)
        vn = vns[0]
        self.assertEqual(vn.id, 17)
        self.assertEqual(vn.title, "Ever17 -the out of infinity-")
        self.assertEqual(vn.original_language, "ja")
        self.assertGreater(vn.length_in_minutes, 30 * 60)
        self.assertGreater(vn.length_vote_count, 70)
        self.assertGreater(vn.image_flagging.vote_count, 5)
        self.assertLess(vn.image_flagging.sexual_avg, 0.5)
        self.assertLess(vn.image_flagging.violence_avg, 0.5)
        self.assertEqual(vn.image_width, 256)
        self.assertEqual(vn.image_height, 360)
        self.assertGreater(vn.popularity, 40)
        self.assertIsInstance(vn.aliases, list)
        self.assertIn("E17", vn.aliases)
        title_found = False
        for title in vn.titles:
            if title.language == "zh-Hant":
                self.assertEqual(title.title, "Shiguang de Jiban")
                self.assertEqual(title.original_title, "時光的羈絆")
                self.assertTrue(title.official)
                title_found = True
                break
        self.assertTrue(title_found)
        self.assertEqual(len(vn.screens), 10)
        screenshot = vn.screens[0]
        self.assertEqual(screenshot.id, "sf190")
        self.assertEqual(screenshot.width, 800)
        self.assertEqual(screenshot.height, 600)
        self.assertEqual(screenshot.thumbnail, "https://s2.vndb.org/st/90/190.jpg")
        self.assertEqual(screenshot.thumbnail_width, 136)
        self.assertEqual(screenshot.thumbnail_height, 102)
