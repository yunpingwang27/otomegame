from datetime import date
from vndb_thigh_highs.models import Flag, UserVN, BuiltInLabelId
from vndb_thigh_highs.models.operators import and_
from test_case import CommandTest, ResponseTest

class GetUserVNCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(UserVN)

    def test_user_vn_basic(self):
        expected = 'get ulist basic (uid = 144365 and vn = 96)'
        text_command = self.command.make_command(
            and_(UserVN.user_id == 144365, UserVN.vn_id == 96), Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_user_vn_all_flags(self):
        expected = 'get ulist basic (uid = 144365 and vn = 96)'
        text_command = self.command.make_command(
            and_(UserVN.user_id == 144365, UserVN.vn_id == 96), Flag.BASIC)
        self.assertEqual(text_command, expected)

class GetUserVNResponseTest(ResponseTest):
    def test_user_vn(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.user_vn_144365_96(),
        ])
        user_vns = self.vndb.get_ulist(
            and_(UserVN.user_id == 144365, UserVN.vn_id == 96)
        )
        self.assertEqual(len(user_vns), 1)
        user_vn = user_vns[0]
        self.assertEqual(user_vn.user_id, 144365)
        self.assertEqual(user_vn.vn_id, 96)
        self.assertEqual(user_vn.vote, 70)
        self.assertEqual(user_vn.notes, "")
        self.assertEqual(user_vn.started_date, date(2017, 1, 6))
        self.assertEqual(user_vn.finished_date, date(2017, 2, 2))
        self.assertEqual(len(user_vn.labels), 2)
        self.assertEqual(user_vn.labels[0].id, BuiltInLabelId.FINISHED)
        self.assertEqual(user_vn.labels[0].name, "Finished")
        self.assertEqual(user_vn.labels[1].id, BuiltInLabelId.VOTED)
        self.assertEqual(user_vn.labels[1].name, "Voted")
