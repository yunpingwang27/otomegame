from vndb_thigh_highs.models import Flag, Character, VN, Quote
from vndb_thigh_highs import GetCommandOptions
from test_case import CommandTest, ResponseTest

class GetCommandOptionsCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.vn_command = self.get_factory.create_command(VN)
        self.quote_command = self.get_factory.create_command(Quote)

    def test_sort(self):
        expected = 'get vn basic (id = 1) {"sort": "popularity", "reverse": true}'
        options = GetCommandOptions()
        options.sort = VN.popularity
        options.reverse = True
        text_command = self.vn_command.make_command(VN.id == 1, Flag.BASIC, options)
        self.assertEqual(text_command, expected)

    def test_sort_fake_field(self):
        expected = 'get quote basic (id = 1) {"sort": "random"}'
        options = GetCommandOptions()
        options.sort = Quote.random
        text_command = self.quote_command.make_command(Quote.vn_id == 1, options=options)
        self.assertEqual(text_command, expected)

class GetCommandOptionsResponseTest(ResponseTest):
    sengoku_rance_characters_ids = [
        735, 2855, 2872, 2856, 740, 736, 2859, 2862, 2897, 2904,
        2864, 2959, 2861, 2887, 5833, 2877, 2880, 2863, 2956, 2871,
        2958,
    ]

    def test_multiple_pages(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.sengoku_rance_characters_page_1(),
            self.response_factory.sengoku_rance_characters_page_2(),
            self.response_factory.sengoku_rance_characters_page_3(),
        ])
        characters = self.vndb.get_all_character(
            Character.id == self.sengoku_rance_characters_ids, Flag.BASIC)
        self.assertEqual(len(characters), len(self.sengoku_rance_characters_ids))
        unique_ids = set([
            character.id for character in characters
        ])
        self.assertEqual(len(unique_ids), len(self.sengoku_rance_characters_ids))

    def test_limit(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.sengoku_rance_characters_page_1(),
            self.response_factory.sengoku_rance_characters_page_2(),
        ])
        options = GetCommandOptions()
        options.limit = 15
        characters = self.vndb.get_all_character(
            Character.id == self.sengoku_rance_characters_ids,
            Flag.BASIC, options)
        self.assertTrue(len(characters) >= 15)
        self.assertTrue(len(characters) < 50)
        unique_ids = set([
            character.id for character in characters
        ])
        self.assertTrue(len(unique_ids) >= 15)
        self.assertTrue(len(unique_ids) < 50)
