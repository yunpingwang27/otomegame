file = open("all.txt","r",encoding='utf-8')
# row = file.readlines()
# file=open('adm.txt',mode='r',encoding='UTF-8')

contents = file.readlines()
# print(contents[1:10][:])
full = []
for msg in contents:
    msg = msg.strip('\n')
    adm = msg.split(';')
    # for i in adm:
    # if '' in adm:
        # adm.remove('')
    # if 'g542' in adm:
    full.append(adm)
file.close()
# print(full[171:177])



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
# print(len(full))
# print(len(full))
# print(len(i[2]))
print(len(desc_zh))


output = []
for t in range(len(full)):
    out = []
    i = full[t]
    t = '名称：%s,原始语言：%s,平台：%s,发行日期：%s,简介（机翻）：%s,封面图url：%s' % (i[1],i[3],i[4],i[2],desc_zh[t][1],i[-1])
    out.append(i[0])
    out.append(i[1])
    # out.append(i[8])
    out.append(t)
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
