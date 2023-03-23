import unittest
from vndb_thigh_highs.models import VN, UserVN, User
from vndb_thigh_highs import GetCommandOptions
from vndb_thigh_highs.error import (
    TableUsedError, ErrorResponseError, ErrorResponseErrorId, ResponseError)
from test_case import CommandTest, ResponseTest

class ErrorCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.vn_command = self.get_factory.create_command(VN)
        self.uservn_command = self.set_factory.create_command(UserVN)

    def test_sort_error(self):
        options = GetCommandOptions()
        options.sort = User.id
        try:
            self.vn_command.make_command(VN.id == 1, options=options)
            self.assertTrue(False)
        except TableUsedError as e:
            self.assertTrue(True)

    def test_filter_error(self):
        try:
            self.vn_command.make_command(User.id == 1)
            self.assertTrue(False)
        except TableUsedError as e:
            self.assertTrue(True)

    def test_set_error(self):
        try:
            self.uservn_command.make_command(1297, {
                User.id: 100
            })
            self.assertTrue(False)
        except TableUsedError as e:
            self.assertTrue(True)

class ErrorResponseTest(ResponseTest):
    @unittest.skipUnless(
        ResponseTest.use_mock_socket,
        "This test is long because the server asks a long wait time.")
    def test_throttled(self):
        iterations = 100
        self.socket.add([
            self.response_factory.ok(),
        ] + iterations * [
            self.response_factory.vn_17(),
        ] + [
            self.response_factory.error_throttled(),
        ] + iterations * [
            self.response_factory.vn_17(),
        ])
        for i in range(0, iterations * 2):
            self.vndb.get_vn(VN.id == 17)
        self.assertTrue(True)

    def test_need_login_error(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.error_need_login(),
        ])
        try:
            self.vndb.set_ulist(17, {
                UserVN.vote: 100,
            })
            self.assertTrue(False)
        except ErrorResponseError as e:
            self.assertEqual(e.id, ErrorResponseErrorId.NEED_LOGIN)

    @unittest.skipUnless(
        ResponseTest.use_mock_socket,
        "Server works fine")
    def test_unknown_response_error(self):
        self.socket.add([
            self.response_factory.unknown_response(),
        ])
        try:
            self.vndb.login()
        except ResponseError as e:
            self.assertEqual(str(e), "Unknown response 'invalid'")

    @unittest.skipUnless(
        ResponseTest.use_mock_socket,
        "Server works fine")
    def test_error_unknown_response_error(self):
        self.socket.add([
            self.response_factory.error_unknown(),
        ])
        try:
            self.vndb.login()
        except ValueError as e:
            self.assertEqual(str(e), "'v17' is not a valid <enum 'ErrorResponseErrorId'>")
