file = open("trans.test","r",encoding='utf-8')
contents = file.readlines()
# print(contents[1:10][:])
admin = []
for msg in contents:
    msg = msg.strip('\n')
    adm = msg.split(';')
    if '"src_text":""' in adm[1]:
        adm[1] = ''
    admin.append(adm)
# print(admin[0:5])
file.close()
# for i in admin:
    # if 
with open('desc_trans.txt','w',encoding='utf-8') as f:
# with open('otomevn_full.txt','w') as f:
    for i in admin:
        for j in i:
            f.write(j)
            f.write(';')
        f.write('\n')
    f.close()