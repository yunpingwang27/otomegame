from vndb_thigh_highs.models import Flag, Producer
from test_case import CommandTest, ResponseTest

class GetProducerCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(Producer)

    def test_producer_basic(self):
        expected = 'get producer basic (id = 428)'
        text_command = self.command.make_command(Producer.id == 428, Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_producer_all_flags(self):
        expected = 'get producer basic,details,relations (id = 350)'
        text_command = self.command.make_command(Producer.id == 350)
        self.assertEqual(text_command, expected)

class GetProducerResponseTest(ResponseTest):
    def test_producer(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.producer_428(),
        ])
        producers = self.vndb.get_producer(Producer.id == 428)
        self.assertEqual(len(producers), 1)
        producer = producers[0]
        self.assertEqual(producer.id, 428)
        self.assertEqual(producer.name, "MangaGamer")
        self.assertEqual(producer.links.homepage, "http://www.mangagamer.com/")
