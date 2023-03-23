file2 = open("./otomevnid.txt","r",encoding='utf-8')

contents = file2.readlines()
otomevn = []
for msg in contents:
    msg = msg.strip('\n')
    otomevn.append(msg)
file2.close()
from vndb_thigh_highs.cache import Cache
from vndb_thigh_highs import VNDB, Config

config = Config()
config.cache = Cache("./test.json")
config.set_session("destinydream", 'fed39c06b0884118c1526405b9d6fe85cd52cb75')

vndb = VNDB(config=config)
db_stats = vndb.dbstats()
from vndb_thigh_highs.models import VN
from vndb_thigh_highs.models import Flag

# r = VN.staff
# from vndb_thigh_highs import GetCommandOptions
vn = vndb.get_all_vn(VN.tags == 542,[Flag.BASIC,Flag.DETAILS])
# vn = vndb.get_all_vn(VN.id == 17,[Flag.BASIC,Flag.DETAILS])
# print(vn.values())
# vndb.get_all_vn(VN.id == 17, [Flag.BASIC,Flag.DETAILS])
# 读取json文件内容,返回字典格式
import json

# with open('./test.json','r',encoding='utf8')as fp:
#     json_data = json.load(fp)

# 处理嵌套json文件中指定关键字
# 处理字典值
def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list

    for value in dic.values():  # 传入数据不符合则对其value值进行遍历
        if isinstance(value, dict):
            get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
        elif isinstance(value, (list, tuple)):
            _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
    return tmp_list


# 处理元组或列表值
def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(val_, (list, tuple)):
            _get_value(key, val_, tmp_list)


def main():
    # file_list = os.listdir(r"./json_files")
    # print(file_list)
    
    # for filename in file_list:
    with open('./test.json', 'r') as load_f:
        json_data = json.load(load_f)  # json files to dict:json_data
    # dict_test = {}
    game = json_data["get vn basic,details (id = 17) {\"page\": 1}"]
    items = game["items"]
    items = items[0]
    platforms = items["platforms"]
    print(platforms)
    # platforms = items["platforms"]
    # platforms_values = get_target_value('platforms', json_data, [])  # 利用json文件中的shape_attributes关键字可对应圈出的框的数量
    # platforms['platforms'] = platforms_values
    # description = get_target_value('description',json_data)
    # print(platforms)
    number_count = len(items)
    # print("file:", filename)
    print("numbers:", number_count)


if __name__ == '__main__':
    main()


    # print('这是文件中的json数据：',json_data)
    # print('这是读取到文件数据的数据类型：', type(json_data))
# print(json_data.keys)
# print(json_data['title'])
# print(vn)
# vn.id
# vnid = []
# for i in vns:
    # vnid.append(i.id)
# options = GetCommandOptions()
# options.sort = VN.released_date
# options.reverse = True
# vndb.get_vn(VN.id == 17, Flag.BASIC, options)
# vndb.get_vn(VN.id == 17, options=options)

# options = GetCommandOptions()
# options.sort = VN.released_date
# options.reverse = True
# options.limit = 50 # get_all option, stops once at least 50 entries are received
# vndb.get_all_vn(VN.id != 17, options=options)

# from datetime import date
# from vndb_thigh_highs.models import UserVN, BuiltInLabelId


