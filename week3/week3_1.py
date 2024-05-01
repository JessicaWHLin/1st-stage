import urllib.request as request
import json
import re
import csv
import copy
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
with request.urlopen(src) as response:
    spot=json.load(response)
# print(spot)
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
with request.urlopen(src) as response:
    mrt=json.load(response)
# print(mrt)

#找出捷運站的資訊:[站名,地址,serial_no]
mrt_info=[]
mrt_info_no=[]
for i in mrt.keys():
    mrt_info=mrt['data']
# print(len(mrt_info))
for i in range(len(mrt_info)):
    mrt_info_no.append([mrt_info[i]['MRT'],mrt_info[i]['address'],mrt_info[i]['SERIAL_NO']])
# print(mrt_info_no)
#精簡MRT地址→行政區
for i in range(len(mrt_info_no)):
    mrt_info_no[i][1]=mrt_info_no[i][1][5:8]  
# for i in range(len(mrt_info_no)):
# print(mrt_info_no)

#取出要放在CSV的資料
spot_info=[]
spot_info_no=[]
for i in spot.keys():
    for j in spot['data'].keys():
        spot_info=spot['data']['results']
# print(spot_info[0])
for i in range(len(spot_info)):
    spot_info_no.append([spot_info[i]['stitle'],spot_info[i]['SERIAL_NO'],spot_info[i]['longitude'],spot_info[i]['latitude']])
# print(len(spot_info)) #58
# print(len(spot_info_no[0]))#5
#處理image的網址,取第一個 # re.research(pattern,string,flags=0)
images=[]
match=[]
pattern = r"https?://\S+?\.(?:jpg|JPG)"
for i in range(len(spot_info_no)): #58
    images.append(spot_info[i]['filelist'])
    match=re.search(pattern,images[i])
# print(images[0:2])
    if match:
        url=match.group()
        spot_info_no[i].append(url)
spot_info_copy=copy.deepcopy(spot_info_no)
# print(spot_info_copy[0])
for i in range(len(spot_info_no)):
    for j in range(len(mrt_info_no)):
        if spot_info_no[i][1] == mrt_info_no[j][2]:
            spot_info_no[i][1]= mrt_info_no[j][1]
            spot_info_copy[i][1]=mrt_info_no[j][0]
# 按MRT分群spot

mrt_group=[]
mrt_group_final=[]
for i in range(len(mrt_info_no)):
    if mrt_info_no[i][0] not in mrt_group:
        mrt_group.append(mrt_info_no[i][0]) #32  
    else:
        continue
for i in range(len(mrt_group)):
    mrt_group_final.append([mrt_group[i]])

for i in range(len(mrt_group)):
    for j in range(len(spot_info_copy)):
        if spot_info_copy[j][1]== mrt_group[i]:
            mrt_group_final[i].append(spot_info_copy[j][0])
        else:
            continue

      
#寫入spot.csv
with open("spot.csv", mode="w", newline="",encoding="utf-8-sig") as file:
    writer=csv.writer(file)
    for i in range(len(spot_info_no)):
        writer.writerow(spot_info_no[i])

with open("mrt.csv", mode="w", newline="",encoding="utf-8-sig") as file:
    writer=csv.writer(file)
    for i in range(len(mrt_group_final)):
        writer.writerow(mrt_group_final[i])
