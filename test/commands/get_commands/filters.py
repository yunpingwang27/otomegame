from vndb_thigh_highs.models import VN
from vndb_thigh_highs.models.operators import and_, or_, search
from test_case import TestCase

class FilterTest(TestCase):
    def test_eq(self):
        filters = VN.id == 1
        self.assertEqual(str(filters), 'id = 1')

    def test_ne(self):
        filters = VN.id != 1
        self.assertEqual(str(filters), 'id != 1')

    def test_le(self):
        filters = VN.released_date <= 2010
        self.assertEqual(str(filters), 'released <= 2010')

    def test_lt(self):
        filters = VN.released_date < 2010
        self.assertEqual(str(filters), 'released < 2010')

    def test_ge(self):
        filters = VN.released_date >= 2010
        self.assertEqual(str(filters), 'released >= 2010')

    def test_gt(self):
        filters = VN.released_date > 2010
        self.assertEqual(str(filters), 'released > 2010')


    def test_eq_integer_array(self):
        filters = VN.id == [1, 2, 3]
        self.assertEqual(str(filters), 'id = [1, 2, 3]')

    def test_ne_integer_array(self):
        filters = VN.id != [2, 5, 1]
        self.assertEqual(str(filters), 'id != [2, 5, 1]')


    def test_eq_str(self):
        filters = VN.title == 'fsn'
        self.assertEqual(str(filters), 'title = "fsn"')

    def test_eq_str_with_special_char(self):
        filters = VN.title == 'f/sn'
        self.assertEqual(str(filters), 'title = "f/sn"')


    def test_eq_string_array(self):
        filters = VN.languages == ["en", "ja"]
        self.assertEqual(str(filters), 'languages = ["en", "ja"]')

    def test_ne_string_array(self):
        filters = VN.languages != ["en", "ja"]
        self.assertEqual(str(filters), 'languages != ["en", "ja"]')


    def test_and(self):
        filters = and_(VN.id == 1, VN.id != 8)
        self.assertEqual(str(filters), 'id = 1 and id != 8')

    def test_or(self):
        filters = or_(VN.id == 1, VN.id != 8)
        self.assertEqual(str(filters), 'id = 1 or id != 8')

    def test_search_title(self):
        filters = search(VN.title, 'ever17')
        self.assertEqual(str(filters), 'title ~ "ever17"')


    def test_search(self):
        filters = search(VN.search, 'ever17')
        self.assertEqual(str(filters), 'search ~ "ever17"')

    def test_null(self):
        filters = VN.original_title == None
        self.assertEqual(str(filters), 'original = null')

    def test_column_as_right_parameter(self):
        filters = 1 == VN.id
        self.assertEqual(str(filters), 'id = 1')

    def test_huge(self):
        filters = or_(
            and_(
                search(VN.title, "imopara"),
                VN.id > 5,
                VN.id < 100
            ),
            and_(
                VN.firstchar == 'F',
                VN.platforms == ["ps2", "ps4"]
            )
        )
        expected = '(title ~ "imopara" and id > 5 and id < 100) or (firstchar = "F" and platforms = ["ps2", "ps4"])'
        self.assertEqual(str(filters), expected)
