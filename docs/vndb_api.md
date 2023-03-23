# VNDB Thigh-highs API

## Getting started
You need to instanciate the main vndb object to interface the database.
```
from vndb_thigh_highs import VNDB
vndb = VNDB()
```

## Using a user
If you want to login using your user do the following:
```
from vndb_thigh_highs import VNDB, Config

config = Config()
config.set_login("your_username", "your_password")
vndb = VNDB(config=config)
```

If you want to get a session token:
```
config = Config()
config.set_login("your_username", "your_password")
config.set_create_session(True)
vndb = VNDB(config=config)
session_token = vndb.login()
```

You can then login using the session token:
```
config = Config()
config.set_session("your_username", session_token)
vndb = VNDB(config=config)
```

To logout and close the session:
```
vndb.logout()
```

## DB Stats
To get the database statistics:
```
db_stats = vndb.dbstats()
```

## Get commands
Get commands are available for the following objects:
- VN
- Release
- Producer
- Character
- Staff
- User
- User VN list
- User VN list labels
- Quote

Vnlist, votelist and wishlist are no longer supported, use the ulist command instead.

The following line will retrieve a VN list matching the given filter
```
from vndb_thigh_highs.models import VN

vns = vndb.get_vn(VN.id == 17)
```

The line above will perform only one request, it may not contains all the data you want. If you are retrieving a large number of entries get all matching entries by using:
```
vns = vndb.get_all_vn(VN.id != 17)
```

Here is a quick list of all get commands:
```
vns = vndb.get_vn(VN.id == 1)
vns = vndb.get_all_vn(VN.id == 1)

releases = vndb.get_release(Release.id == 1)
releases = vndb.get_all_release(Release.id == 1)

producers = vndb.get_producer(Producer.id == 1)
producers = vndb.get_all_producer(Producer.id == 1)

characters = vndb.get_character(Character.id == 1)
characters = vndb.get_all_character(Character.id == 1)

staffs = vndb.get_staff(Staff.id == 1)
staffs = vndb.get_all_staff(Staff.id == 1)

users = vndb.get_user(User.id == 1)
users = vndb.get_all_user(User.id == 1)

user_vns = vndb.get_ulist(UserVN.user_id == 1)
user_vns = vndb.get_all_ulist(UserVN.user_id == 1)

user_labels = vndb.get_ulist_labels(UserLabel.user_id == 1)
user_labels = vndb.get_all_ulist_labels(UserLabel.user_id == 1)

quotes = vndb.get_quote(Quote.vn_id == 1)
quotes = vndb.get_all_quote(Quote.vn_id == 1)
```

### Filters
Various filters can be used to perform the request:
```
from vndb_thigh_highs.models.operators import and_, or_, search

vndb.get_vn(VN.id == 17)
vndb.get_vn(VN.id == [17, 18])
vndb.get_vn(VN.id <= 5)

vndb.get_vn(search(VN.title, "ever17")) # '~' operator

vndb.get_vn(and_(VN.id == 17, VN.firstchar == 'E'))
vndb.get_vn(or_(VN.id == 17, VN.firstchar == 'E'))
```

If you don't feel like using this syntax, you can pass the string representing the filter you want.
```
vndb.get_vn("id = 17")
```

### Flags
By default all data is requested, if only some specific data is needed use the flags:
```
from vndb_thigh_highs.models import Flag

vndb.get_vn(VN.id == 17, Flag.BASIC)
vndb.get_vn(VN.id == 17, [Flag.BASIC, Flag.DETAILS])
```

### Options
If you need to use options:
```
from vndb_thigh_highs import GetCommandOptions

options = GetCommandOptions()
options.sort = VN.released_date
options.reverse = True
vndb.get_vn(VN.id == 17, Flag.BASIC, options)
vndb.get_vn(VN.id == 17, options=options)

options = GetCommandOptions()
options.sort = VN.released_date
options.reverse = True
options.limit = 50 # get_all option, stops once at least 50 entries are received
vndb.get_all_vn(VN.id != 17, options=options)
```

## Set commands
Set commands are available for the following objects:
- User VN list

Vnlist, votelist and wishlist are no longer supported, use the ulist command instead.

Use the following line to add or update an entry:
```
from datetime import date
from vndb_thigh_highs.models import UserVN, BuiltInLabelId

vndb.set_ulist(vn_id, {
    UserVN.notes: "adding a vn",
    UserVN.started_date: date(2020, 1, 1),
    UserVN.vote: 100,
    UserVN.labels: [
        BuiltInLabelId.FINISHED,
    ],
})
```

You may specify only the fields to update in the dictionnary.

Use this line to delete an entry:
```
vndb.delete_ulist(vn_id)
```

## Using models
This module uses models to represent the data received, some fields have been renamed or adapted so that the code written is easier to read. For example, the VN object has no 'original' attribute. Instead it has an 'original_title' attribute. If you feel that an attribute is missing, chances are it exists under a different name.

You can check the attributes available for each model in the source code [here](https://code.blicky.net/FoieGras/vndb-thigh-highs/src/branch/master/vndb_thigh_highs/models).

## Cache
A cache option can be used, this is useful when testing a new script to avoid spaming. Get command results are cached as long as the file exists.

```
from vndb_thigh_highs.cache import Cache

config = Config()
config.cache = Cache("path/to/cache/file")
vndb = VNDB(config=config)
```
