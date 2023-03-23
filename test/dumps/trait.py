import os
import unittest
from vndb_thigh_highs.dumps import TraitDatabaseBuilder
from context import abspath
from test_case import TestCase

TRAITS_ARCHIVE_PATH = abspath('../data/traits.json.gz')
TRAITS_JSON_PATH = abspath('../data/traits.json')

class TraitTest(TestCase):
    @unittest.skipUnless(os.path.isfile(TRAITS_JSON_PATH), "Missing data")
    def test_json_file(self):
        builder = TraitDatabaseBuilder()
        trait_database = builder.build_with_json_file(TRAITS_JSON_PATH)
        trait = trait_database.get_trait(114)
        self.assertEqual(trait.name, "Violet")
        self.assertTrue(trait.searchable)
        self.assertTrue(trait.searchable)
        self.assertEqual(len(trait.parents), 1)
        self.assertEqual(len(trait.children), 0)
        for parent_trait in trait.parents:
            self.assertEqual(parent_trait.name, "Eye Color")
            self.assertFalse(parent_trait.searchable)
            self.assertFalse(parent_trait.applicable)

    @unittest.skipUnless(os.path.isfile(TRAITS_ARCHIVE_PATH), "Missing data")
    def test_archive_file(self):
        builder = TraitDatabaseBuilder()
        trait_database = builder.build_with_archive(TRAITS_ARCHIVE_PATH)
        trait = trait_database.get_trait(186)
        self.assertEqual(trait.name, "Thigh-high Stockings")
        self.assertTrue(trait.searchable)
        self.assertTrue(trait.searchable)
        self.assertEqual(len(trait.parents), 1)
        self.assertTrue(len(trait.children) > 3)
