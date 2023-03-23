from datetime import date
from vndb_thigh_highs.error import TableUsedError
from vndb_thigh_highs.models import User, UserVN, BuiltInLabelId
from vndb_thigh_highs.models.operators import and_
from test_case import CommandTest, LoggedInResponseTest

class SetUserVNCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.set_factory.create_command(UserVN)

    def test_set_uservn(self):
        expected = 'set ulist 17 {"notes": "Adding this via tests", "started": "2020-01-01", "finished": "2020-01-02", "vote": 100, "labels": [2]}'
        text_command = self.command.make_command(17, {
            UserVN.notes: "Adding this via tests",
            UserVN.started_date: date(2020, 1, 1),
            UserVN.finished_date: date(2020, 1, 2),
            UserVN.vote: 100,
            UserVN.labels: [
                BuiltInLabelId.FINISHED,
            ],
        })
        self.assertEqual(text_command, expected)

    def test_delete_uservn(self):
        expected = 'set ulist 17'
        text_command = self.command.make_command(17, None)
        self.assertEqual(text_command, expected)

class SetUserVNResponseTest(LoggedInResponseTest):
    def test_set_vn(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.ok(),
            self.response_factory.user_vn_144365_12876(),
            self.response_factory.ok(),
        ])
        vn_id = 12876
        self.add_user_vn(vn_id)
        self.assert_user_vn_is_present(vn_id)
        self.delete_user_vn(vn_id)

    def add_user_vn(self, vn_id):
        self.vndb.set_ulist(vn_id, {
            UserVN.notes: "Adding this via tests",
            UserVN.started_date: date(2020, 1, 1),
            UserVN.finished_date: date(2020, 1, 2),
            UserVN.vote: 100,
            UserVN.labels: [
                BuiltInLabelId.FINISHED,
            ],
        })

    def assert_user_vn_is_present(self, vn_id):
        user_vns = self.vndb.get_ulist(
            and_(UserVN.user_id == 0, UserVN.vn_id == vn_id)
        )
        user_vn = user_vns[0]
        self.assertEqual(user_vn.vn_id, vn_id)
        self.assertEqual(user_vn.notes, "Adding this via tests")
        self.assertEqual(user_vn.started_date, date(2020, 1, 1))
        self.assertEqual(user_vn.finished_date, date(2020, 1, 2))
        self.assertEqual(user_vn.vote, 100)
        self.assertEqual(len(user_vn.labels), 2)
        self.assertEqual(user_vn.labels[0].id, BuiltInLabelId.FINISHED)
        self.assertEqual(user_vn.labels[0].name, "Finished")
        self.assertEqual(user_vn.labels[1].id, BuiltInLabelId.VOTED)
        self.assertEqual(user_vn.labels[1].name, "Voted")

    def delete_user_vn(self, vn_id):
        self.vndb.delete_ulist(vn_id)
