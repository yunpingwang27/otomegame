import unittest
from vndb_thigh_highs.login_command import LoginCommand, LoginConfig
from vndb_thigh_highs.error import ErrorResponseError, ErrorResponseErrorId
from test_case import CommandTest, ResponseTest, ResponseTestWithPassword

class LoginCommandTest(CommandTest):
    def test_login_without_user(self):
        expected = 'login {"protocol": 1, "client": "VNDB Thigh-highs", "clientver": "0.x-test"}'
        login_config = LoginConfig(self.config)
        command = LoginCommand(self.socket, login_config)
        text_command = command.make_login_command()
        self.assertEqual(text_command, expected)

    def test_login_with_user(self):
        expected = 'login {"protocol": 1, "client": "VNDB Thigh-highs", "clientver": "0.x-test", "username": "foiegras", "password": "not_foiegras_password"}'
        login_config = LoginConfig(self.config)
        login_config.set_login("foiegras", "not_foiegras_password")
        command = LoginCommand(self.socket, login_config)
        text_command = command.make_login_command()
        self.assertEqual(text_command, expected)

    def test_login_with_create_session(self):
        expected = 'login {"protocol": 1, "client": "VNDB Thigh-highs", "clientver": "0.x-test", "username": "foiegras", "password": "not_foiegras_password", "createsession": true}'
        login_config = LoginConfig(self.config)
        login_config.set_login("foiegras", "not_foiegras_password")
        login_config.set_create_session(True)
        command = LoginCommand(self.socket, login_config)
        text_command = command.make_login_command()
        self.assertEqual(text_command, expected)

    def test_login_with_session_token(self):
        expected = 'login {"protocol": 1, "client": "VNDB Thigh-highs", "clientver": "0.x-test", "username": "foiegras", "sessiontoken": "c97e1f0c9f1d59ab67d2"}'
        login_config = LoginConfig(self.config)
        login_config.set_session("foiegras", "c97e1f0c9f1d59ab67d2")
        command = LoginCommand(self.socket, login_config)
        text_command = command.make_login_command()
        self.assertEqual(text_command, expected)

    def test_logout(self):
        expected = 'logout'
        login_config = LoginConfig(self.config)
        command = LoginCommand(self.socket, login_config)
        text_command = command.make_logout_command()
        self.assertEqual(text_command, expected)

class LoginResponseTest(ResponseTest):
    def test_simple_login_without_user(self):
        self.socket.add([
            self.response_factory.ok(),
        ])
        self.vndb.login()
        self.assertTrue(True)

    def test_double_login_without_user(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.ok(),
        ])
        self.vndb.login()
        self.vndb.disconnect()
        self.vndb.login()
        self.assertTrue(True)

    @unittest.skipUnless(
        ResponseTest.use_mock_socket,
        "Testing too many times causes the server to refuse future login.")
    def test_auth_error(self):
        self.socket.add([
            self.response_factory.error_auth(),
        ])
        try:
            self.vndb.config.set_login("foiegras", "not_foiegras_password")
            self.vndb.login()
            self.assertTrue(False)
        except ErrorResponseError as e:
            self.assertEqual(e.id, ErrorResponseErrorId.AUTH)

    def test_already_logged_in_error(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.error_logged_in(),
        ])
        try:
            self.vndb.login()
            self.vndb.login()
            self.assertTrue(False)
        except ErrorResponseError as e:
            self.assertEqual(e.id, ErrorResponseErrorId.LOGGED_IN)

class LoginWithUserResponseTest(ResponseTestWithPassword):
    def test_login_with_user(self):
        self.socket.add([
            self.response_factory.ok(),
        ])
        self.vndb.config.set_login(self.username, self.password)
        self.vndb.login()
        self.assertTrue(True)

    def test_create_session(self):
        self.socket.add([
            self.response_factory.session(),
        ])
        self.vndb.config.set_login(self.username, self.password)
        self.vndb.config.set_create_session(True)
        session_token = self.vndb.login()
        self.assertTrue(session_token is not None)
        self.assertEqual(len(session_token), 40)

    def test_login_with_session_token(self):
        self.socket.add([
            self.response_factory.session(),
            self.response_factory.ok(),
            self.response_factory.ok(),
        ])
        self.vndb.config.set_login(self.username, self.password)
        self.vndb.config.set_create_session(True)
        session_token = self.vndb.login()
        self.vndb.disconnect()
        self.vndb.config.set_login(None, None)
        self.vndb.config.set_create_session(None)
        self.vndb.config.set_session(self.username, session_token)
        self.vndb.login()
        self.vndb.logout()
