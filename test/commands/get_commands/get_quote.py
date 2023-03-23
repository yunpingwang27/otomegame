from vndb_thigh_highs.models import Flag, Quote
from test_case import CommandTest, ResponseTest

class GetQuoteCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(Quote)

    def test_quote_basic(self):
        expected = 'get quote basic (id = 17)'
        text_command = self.command.make_command(Quote.vn_id == 17, Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_quote_all_flags(self):
        expected = 'get quote basic (id >= 1)'
        text_command = self.command.make_command(Quote.vn_id >= 1)
        self.assertEqual(text_command, expected)

class GetQuoteResponseTest(ResponseTest):
    def test_quote(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.quote_1299(),
        ])
        quotes = self.vndb.get_quote(Quote.vn_id == 1299)
        self.assertEqual(len(quotes), 3)
        expected = [
            "Right here. The paperwork is here inside my heart.",
            "Nonsense, filth, codswallop, FLIMFLAM!",
            "His daughter had been kidnapped, and he was stuck unclogging a toilet.",
        ]
        for quote in quotes:
            self.assertEqual(quote.vn_id, 1299)
            self.assertEqual(quote.vn_title, "428 ~Fuusa Sareta Shibuya de~")
            self.assertIn(quote.quote, expected)
