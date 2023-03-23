#!/bin/env python

import unittest
import context

from dumps.tag import TagTest
from dumps.trait import TraitTest
from dumps.vote import VoteTest

from commands.login import (
    LoginCommandTest, LoginResponseTest, LoginWithUserResponseTest)
from commands.dbstats import DBStatsCommandTest, DBStatsResponseTest
from commands.error import ErrorCommandTest, ErrorResponseTest

from commands.get_commands.filters import FilterTest
from commands.get_commands.options import (
    GetCommandOptionsCommandTest, GetCommandOptionsResponseTest)
from commands.get_commands.get_vn import (
    GetVNCommandTest, GetVNResponseTest)
from commands.get_commands.get_release import (
    GetReleaseCommandTest, GetReleaseResponseTest)
from commands.get_commands.get_producer import (
    GetProducerCommandTest, GetProducerResponseTest)
from commands.get_commands.get_character import (
    GetCharacterCommandTest, GetCharacterResponseTest)
from commands.get_commands.get_staff import (
    GetStaffCommandTest, GetStaffResponseTest)
from commands.get_commands.get_user import (
    GetUserCommandTest, GetUserResponseTest)
from commands.get_commands.get_user_label import (
    GetUserLabelCommandTest, GetUserLabelResponseTest)
from commands.get_commands.get_user_vn import (
    GetUserVNCommandTest, GetUserVNResponseTest)
from commands.get_commands.get_quote import (
    GetQuoteCommandTest, GetQuoteResponseTest)

from commands.set_commands.set_user_vn import (
    SetUserVNCommandTest, SetUserVNResponseTest)

def main():
    unittest.main()

if __name__ == '__main__':
    main()
