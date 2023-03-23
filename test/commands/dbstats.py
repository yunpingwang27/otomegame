from vndb_thigh_highs.dbstats_command import DBStatsCommand
from test_case import CommandTest, ResponseTest

class DBStatsCommandTest(CommandTest):
    def test_dbstats(self):
        expected = 'dbstats'
        command = DBStatsCommand(self.socket)
        text_command = command.make_command()
        self.assertEqual(text_command, expected)

class DBStatsResponseTest(ResponseTest):
    def test_dbstats(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.dbstats(),
        ])
        dbstats = self.vndb.dbstats()
        self.assertTrue(dbstats.releases > 50000)
        self.assertTrue(dbstats.characters > 70000)
