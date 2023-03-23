import json
with open('./otome_al.json', 'r') as load_f:
    json_data = json.load(load_f)  # json files to dict:json_data



s = "get vn basic,details (tags = \"542\") {\"page\": "+str(1)+"}"

items_dict = {}
items_list = []
for i in range(1,len(json_data)+1):
    s = 'get vn anime,basic,details,relations,screens,staff,stats,tags,titles (tags = \"542\") {\"page\": '+str(i)+'}'
    game = json_data[s]
    # items_list['otomes'] = game
    items = game["items"]
    items_list.append(items)
# print(items_list[0:5]))
items_list_n = []
for i in range(len(items_list)):
    for j in range(len(items_list[i])):
        items_list_n.append(items_list[i][j])
# print(len(items_list_n))
items_dict_a = {}
items_dict['items'] = items_list_n
# items_dict_a['otome'] = items_dict
    # print(len(items))
    # for j in 
    # t = json.dumps(i)
        # items_list.append(t)

with open("items_al.json","w") as outfile:
        json.dump(items_dict,outfile,sort_keys=True)

# items = items[0]

# platforms = items["platforms"]
# print(platforms)