import json

from numpy import ones
# with open('./items_1.json', 'r') as load_f:
with open('./data_otome/items_al.json', 'r') as load_f:
    
    json_data = json.load(load_f)  # json files to dict:json_data

items = json_data['items']
# print(len(items))
id = []
description = []
title = []
for i in items:
    id.append(i['id'])
    description.append(i['description'])
    title.append(i['title'])

def write_list(con,items):
    lisr = []
    # id = []
    for i in items:
        if i[con] == None:
            lisr.append('n')
        if isinstance(i[con],list):
            if len(i[con]) == 1:
                lisr.append(i[con][0])
            else:
                # if 
                j = ','.join(i[con])
                lisr.append(j)
        else:
            lisr.append(i[con])
        # id.append(i['id'])
            # lisr.append(i[con])
    return lisr
    # filename = con+'.txt'
    # with open(filename,'w',encoding='utf-8') as f:
    #     for i in range(len(id)):
    #         # for j in i:
    #         f.write(str(id[i]))
    #         f.write(';')
    #         if isinstance(lisr[i],list):
    #             for j in lisr[i]:
    #                 f.write(str(j))
    #                 f.write(',')
    #         else:
    #             f.write(str(lisr[i]))              
    #         f.write('\n')
    # f.close()

# print(list(items[0])[0])
id = write_list(con='id',items=items)
title = write_list(con='title',items=items)
# titles = write_list(con='titles',items=items)
released = write_list(con = 'released',items=items)
image = write_list(con = 'image',items=items)
orig_lang = write_list(con='orig_lang',items=items)
languages = write_list(con='languages',items=items)
platforms = write_list(con='platforms',items=items)
description = write_list(con='description',items=items)
# print(description[0:5])
all_otome = []
for i in range(len(id)):
        if description[i] == None:
            description[i] = 'n'
            # f.write('')
        else:
            # description[i] = description[i].replace('\n\n[',';[')
            description[i] = description[i].replace('\n','\t')
set_titles = []
# print(len(items))
for j in items:
    titles = j['titles']
    ti = []
    for i in range(len(titles)):
        if titles[i] == None:
            titles[i] = 'n'
            # f.write('')
        else:
            # for s in titles[i]:
            ti.append(titles[i]['title'])
                # ti.append(titles)
    sti = '##'.join(ti)
    set_titles.append(sti)

            # description[i] = description[i].replace('\n\n[',';[')
            # titles[i] = description[i].replace('\n','\t')
print(len(set_titles))

for i in range(len(id)):
    otome = list(ones(9))
    # for i in range(7):
    otome[0] = id[i]
    otome[1] = title[i]
    otome[2] = released[i]
    otome[3] = orig_lang[i]
    otome[4] = platforms[i]
    otome[5] = languages[i]
    otome[6] = image[i]
    otome[7] = description[i]
    # otome[8] = set_titles[i]
        # otome.append(id[i])
    # otome.append(title[i])
    # otome.append(released[i])
    # otome.append(orig_lang[i])
    # otome.append(platforms[i])
    # otome.append(languages[i])
    # otome.append(image[i])
    # otome.append(description[i])
    all_otome.append(otome)





# print(all_otome[0])
with open('all.txt','w',encoding='utf-8') as f:
    for i in all_otome:
        for j in i:
            f.write(str(j))
            f.write('、')
        f.write('\n')
    f.close()
# with open('otomevn_all_otome.txt','w') as f:
    # for i in range(len(id)):
        # for j in i:
        # f.write(str(id[i]))
        # f.write(';')
        # for j in range(len(all_otome[0])):
            # all_otome[6] = all_otome[6].split('\n\n')
            # for s in range(len(all_otome[i][j])):
                # f.write(j)
                # if s != len(j)-1:
                    # f.write(';')
                # else:
                    # pass
            # f.write[';']
            
                # f.writ
        # if all_otome[i] == None:
            # f.write('')
        # else:
            # description[i] = description[i].replace('\n\n',';')
            # f.write(description[i])
        # f.write('\n')
    f.close()

    # for j in i:
    # f.write(str(id[i]))
    # f.write(';')
    # if isinstance(lisr[i],list):
        # for j in lisr[i]:
            # f.write(str(j))
            # f.write(',')

# with open('title.txt','w',encoding='utf-8') as f:
# # with open('otomevn_all_otome.txt','w') as f:
#     for i in range(len(id)):
#         # for j in i:
#         f.write(str(id[i]))
#         f.write(';')
#         f.write(title[i])
#         f.write('\n')
#     f.close()
# print(len(description))
with open('description.txt','w',encoding='utf-8') as f:
# with open('otomevn_all_otome.txt','w') as f:
    for i in range(len(id)):
        # for j in i:
        f.write(str(id[i]))
        f.write(';')
        if description[i] == None:
            f.write('')
        else:
            description[i] = description[i].replace('\n\n',' ')
            f.write(description[i])
        f.write('\n')
    f.close()
with open('titles.txt','w',encoding='utf-8') as f:
# with open('otomevn_all_otome.txt','w') as f:
    for i in range(len(id)):
        # for j in i:
        f.write(str(id[i]))
        f.write(';')
        if set_titles[i] == None:
            f.write('')
        else:
            # set_titles[i] = set_titles[i].replace('\n\n',';')
            f.write(set_titles[i])
        f.write('\n')
    f.close()

#     file = open("all.txt","r",encoding='utf-8')
# # row = file.readlines()
# # file=open('adm.txt',mode='r',encoding='UTF-8')

# contents = file.readlines()
# # print(contents[1:10][:])
# all_otome = []
# for msg in contents:
#     msg = msg.strip('\n')
#     adm = msg.split(';')
#     # for i in adm:
#     # if '' in adm:
#         # adm.remove('')
#     # if 'g542' in adm:
#     all_otome.append(adm)
# file.close()
# print(all_otome[171:177])

# print(len(platforms))
file = open("desc_trans.txt","r",encoding='utf-8')
# row = file.readlines()
# file=open('adm.txt',mode='r',encoding='UTF-8')

contents = file.readlines()
# print(contents[1:10][:])
desc_zh = []
for msg in contents:
    msg = msg.strip('\n')
    adm = msg.split(';')
    # for i in adm:
    # if '' in adm:
        # adm.remove('')
    # if 'g542' in adm:
    desc_zh.append(adm)
file.close()
print(len(desc_zh))
# desc_zh.append('')

# print(len(all_otome))
# print(len(all_otome))
output = []
for t in range(len(all_otome)):
    out = []
    # i = all_otome[t]
    h = '名称：%s,原始语言：%s,平台：%s,发行日期：%s,简介（机翻）：%s,封面图url：%s' % (title[t],orig_lang[t],platforms[t],released[t],desc_zh[t][1],image[t])
    out.append(id[t])
    out.append(title[t])
    out.append(set_titles[t])
    out.append(h)
    output.append(out)

print(output[0])
with open('all_output.txt','w',encoding='utf-8') as f:
# with open('all_quest.txt','w',encoding='utf-8') as f:
    for i in output:
        for j in i:
            f.write(str(j))
            f.write(';')
        f.write('\n')
    f.close()
