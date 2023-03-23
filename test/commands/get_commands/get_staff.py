from vndb_thigh_highs.models import Flag, Staff
from test_case import CommandTest, ResponseTest

class GetStaffCommandTest(CommandTest):
    def setUp(self):
        super().setUp()
        self.command = self.get_factory.create_command(Staff)

    def test_staff_basic(self):
        expected = 'get staff basic (id = 1)'
        text_command = self.command.make_command(Staff.id == 1, Flag.BASIC)
        self.assertEqual(text_command, expected)

    def test_staff_all_flags(self):
        expected = 'get staff aliases,basic,details,vns,voiced (id = 1)'
        text_command = self.command.make_command(Staff.id == 1)
        self.assertEqual(text_command, expected)

class GetStaffResponseTest(ResponseTest):
    def test_staff(self):
        self.socket.add([
            self.response_factory.ok(),
            self.response_factory.staff_1(),
        ])
        staffs = self.vndb.get_staff(Staff.id == 1)
        self.assertEqual(len(staffs), 1)
        staff = staffs[0]
        self.assertEqual(staff.id, 1)
        self.assertEqual(staff.name, "Urobuchi Gen")
        self.assertIn("scenario writer", staff.description)
        self.assertIn("Nitro+", staff.description)
