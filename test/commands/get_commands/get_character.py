from vndb_thigh_highs.models import Flag, Character, Gender
from test_case import CommandTest, ResponseTest

class GetCharacterCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(Character)

    def test_character_basic(self):
        expected = 'get character basic (id = 4052)'
        text_command = self.command.make_command(Character.id == 4052, Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_character_all_flags(self):
        expected = 'get character basic,details,instances,meas,traits,vns,voiced (id = 4052)'
        text_command = self.command.make_command(Character.id == 4052)
        self.assertEqual(text_command, expected)

class GetCharacterResponseTest(ResponseTest):
    def test_character(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.character_4052(),
        ])
        characters = self.vndb.get_character(Character.id == 4052)
        self.assertEqual(len(characters), 1)
        character = characters[0]
        self.assertEqual(character.id, 4052)
        self.assertEqual(character.name, "Yukimura Anzu")
        self.assertEqual(character.gender, Gender.FEMALE)
        self.assertEqual(character.bust, 69)
        self.assertEqual(character.waist, 46)
        self.assertEqual(character.hip, 73)
        self.assertEqual(character.image_width, 200)
        self.assertEqual(character.image_height, 300)

    def test_spoil_gender(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.character_432(),
        ])
        characters = self.vndb.get_character(Character.id == 432)
        self.assertEqual(len(characters), 1)
        character = characters[0]
        self.assertEqual(character.gender, Gender.MALE)
        self.assertEqual(character.spoil_gender, Gender.FEMALE)

    def test_age_cup_size(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.character_34694(),
        ])
        characters = self.vndb.get_character(Character.id == 34694)
        self.assertEqual(len(characters), 1)
        character = characters[0]
        self.assertEqual(character.cup_size, "AA")
        self.assertEqual(character.age, 9)
