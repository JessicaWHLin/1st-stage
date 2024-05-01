def find_and_print(messages, current_station):
  # your code here
    friend=[]
    myLocation=[]
    dis=[]
    #捷運各站的順序
    stationMRT={
      "Songshan":1,
      "Nanjing Sanmin":2,
      "Taipei Arena":3,
      "Nanjing Fuxing":4,
      "SongJiang Nanjing":5,
      "Zhongshan":6,
      "Beimen":7,
      "Ximen":8,
      "Xiaonanmen":9,
      "Chiang Kai-Shek Memorial Hall":10,
      "Guting":11,
      "Taipower Building":12,
      "Gongguan":13,
      "Wanlong":14,
      "Jingmei":15,
      "Dapingin":16,
      "Qizhang":17,
      "Xindian City Hall":18,
      "Xindian":19,
      "Xiaobitan":17.5
    }         
    for name in messages:
      for key in stationMRT:
        if key in messages[name]:
          friend.append([name,key,stationMRT[key]])
    for i in range(0,len(friend)):
      dis.append([friend[i][0]])
    # print(dis)
    # print(friend)
    for sta in stationMRT:
       if current_station in sta:
          myLocation=[sta,stationMRT[sta]]
    # print(myLocation)

    check=18
    for i in range(len(friend)):
      dis[i].append(abs(myLocation[-1]-friend[i][-1]))
      # print(dis[i][1])
      if friend[i][1]=="Xiaobitan":
        dis[i][1]+=1 #支線加1
    # print(dis)
      if dis[i][1]<=check:
        check=dis[i][1]
    # # print(check)
    for i in range(len(dis)):
      if check==dis[i][1]:
         print(dis[i][0])
    # print(dis)

messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
print("-----------Task 1----------")
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian