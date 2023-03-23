from vndb_thigh_highs.models import Flag, UserLabel
from test_case import CommandTest, ResponseTest

class GetUserLabelCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(UserLabel)

    def test_user_label_basic(self):
        expected = 'get ulist-labels basic (uid = 1)'
        text_command = self.command.make_command(
            UserLabel.user_id == 1, Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_user_label_all_flags(self):
        expected = 'get ulist-labels basic (uid = 1)'
        text_command = self.command.make_command(
            UserLabel.user_id == 1)
        self.assertEqual(text_command, expected)

class GetUserLabelResponseTest(ResponseTest):
    def test_user_label(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.user_label_144365(),
        ])
        user_labels = self.vndb.get_ulist_labels(
            UserLabel.user_id == 144365
        )
        self.assertEqual(len(user_labels), 10)
        label = user_labels[0]
        self.assertEqual(label.label_id, 1)
        self.assertEqual(label.name, "Playing")
        self.assertEqual(label.user_id, 144365)
        self.assertEqual(label.private, False)
