import json
import numpy as np
from numpy import ones
import csv
from vndb_thigh_highs.dumps import TagDatabaseBuilder

builder = TagDatabaseBuilder()

tag_database = builder.build_with_json_file("./data/tags.json")

# with open('./items_1.json', 'r') as load_f:
with open('./data_otome/items_al.json', 'r') as load_f:
    
    json_data = json.load(load_f)  # json files to dict:json_data

items = json_data['items']
# print(len(items))
id = []
# id有3960个
description = []
title = []
tags = []
for i in items:
    id.append(i['id'])
    # description.append(i['description'])
    tags.append(i['tags'])
    title.append(i['title'])
# s = []
s = np.zeros(3960)
for i in tags:
    for tag in i:
        s[tag[0]-1] += tag[1]/3

# print(s[0:10])
des = []
con = []
# ta = tag_database.get_tag(542)
# print(ta.description)
for i in range(3960):
    try:
        ta = tag_database.get_tag(i+1)
        des.append(ta.name)
        con.append(ta.description)
    except KeyError:
        des.append(None)
        con.append(None)


print(des[0:10])
with open('tag_id.csv', mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    for index,r in enumerate(s):
        if con[index] != None:
            con[index] =con[index].replace('\n','   ')
        writer.writerow((index+1,des[index],r,con[index]))
# print(s[540:550])
# print(tags[0])
