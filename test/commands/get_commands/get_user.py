from vndb_thigh_highs.models import Flag, User
from test_case import CommandTest, ResponseTest

class GetUserCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(User)

    def test_user_basic(self):
        expected = 'get user basic (id = 1)'
        text_command = self.command.make_command(User.id == 1, Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_user_all_flags(self):
        expected = 'get user basic (id = 1)'
        text_command = self.command.make_command(User.id == 1)
        self.assertEqual(text_command, expected)

class GetUserResponseTest(ResponseTest):
    def test_user(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.user_2(),
        ])
        users = self.vndb.get_user(User.id == 2, Flag.BASIC)
        self.assertEqual(len(users), 1)
        user = users[0]
        self.assertEqual(user.id, 2)
        self.assertEqual(user.username, "Yorhel")
