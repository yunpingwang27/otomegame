from vndb_thigh_highs.dumps import TagDatabaseBuilder

builder = TagDatabaseBuilder()

tag_database = builder.build_with_json_file("./data/tags.json")

# or
# tag_database = builder.build_with_archive("path/to/tags.json.gz")

otome_tag = tag_database.get_tag(542)
# print(tag)
# print(otome_tag.description)
# 对otome game,输出一个列表
# tagid 权重（个数权重之和）
# 3959个乙女游戏，41573个vn
# 首先提取出vn id - tag数据
# 将tag数据进行计数



# from vndb_thigh_highs.dumps import 