import os
import unittest
from vndb_thigh_highs.dumps import VoteBuilder
from context import abspath
from test_case import TestCase

VOTES_ARCHIVE_PATH = abspath('../data/votes.gz')
VOTES_TEXT_PATH = abspath('../data/votes.txt')

class VoteTest(TestCase):
    @unittest.skipUnless(os.path.isfile(VOTES_TEXT_PATH), "Missing data")
    def test_text_file(self):
        builder = VoteBuilder()
        votes = builder.build_with_text_file(VOTES_TEXT_PATH)
        self.assertTrue(len(votes) > 100000)

    @unittest.skipUnless(os.path.isfile(VOTES_ARCHIVE_PATH), "Missing data")
    def test_archive(self):
        builder = VoteBuilder()
        votes = builder.build_with_archive(VOTES_ARCHIVE_PATH)
        self.assertTrue(len(votes) > 100000)
