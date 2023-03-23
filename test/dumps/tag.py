import os
import unittest
from vndb_thigh_highs.dumps import TagDatabaseBuilder, TagCategory
from context import abspath
from test_case import TestCase

TAGS_ARCHIVE_PATH = abspath('../data/tags.json.gz')
TAGS_JSON_PATH = abspath('../data/tags.json')

class TagTest(TestCase):
    @unittest.skipUnless(os.path.isfile(TAGS_JSON_PATH), "Missing data")
    def test_json_file(self):
        builder = TagDatabaseBuilder()
        tag_database = builder.build_with_json_file(TAGS_JSON_PATH)
        tag = tag_database.get_tag(268)
        self.assertEqual(tag.name, "Only a Single Heroine")
        self.assertEqual(tag.category, TagCategory.CONTENT)
        self.assertTrue(tag.searchable)
        self.assertTrue(tag.applicable)
        self.assertEqual(len(tag.parents), 1)
        self.assertEqual(len(tag.children), 0)
        for parent_tag in tag.parents:
            self.assertEqual(parent_tag.name, "Heroine")
            self.assertFalse(parent_tag.searchable)
            self.assertFalse(parent_tag.applicable)

    @unittest.skipUnless(os.path.isfile(TAGS_ARCHIVE_PATH), "Missing data")
    def test_archive_file(self):
        builder = TagDatabaseBuilder()
        tag_database = builder.build_with_archive(TAGS_ARCHIVE_PATH)
        tag = tag_database.get_tag(854)
        self.assertEqual(tag.name, "Heroine's Clothing and Accessories")
        self.assertEqual(tag.category, TagCategory.CONTENT)
        self.assertFalse(tag.searchable)
        self.assertFalse(tag.applicable)
        self.assertEqual(len(tag.parents), 1)
        self.assertTrue(len(tag.children) > 15)
