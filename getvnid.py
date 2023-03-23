
from vndb_thigh_highs.cache import Cache
from vndb_thigh_highs import VNDB, Config

config = Config()
config.cache = Cache("./test.json")

vndb = VNDB(config=config)
db_stats = vndb.dbstats()
from vndb_thigh_highs.models import VN
from vndb_thigh_highs.models import Flag

r = VN.staff
# from vndb_thigh_highs import GetCommandOptions
# vn = vndb.get_all_vn(VN.tags == '542',[Flag.BASIC,Flag.DETAILS])
# vn
vn_ALL = vndb.get_all_vn(VN.tags == '542')
