#Task1
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

#Task2
# your code here, maybe
schedule=[["Jenny"],["John"],["Bob"]] 
rankPrice=[]
rankRate=[]
elem=[]
def rank(cri,rank): #決定排名
        for i in range(0,len(consultants)):
            elem.append(consultants[i].get(cri))
        elem.sort()
        # print(price)
        for i in range(0,len(consultants)):
            # print(consultants[i]["name"])
            for j in range(0,len(consultants)):
                if elem[i]==consultants[j][cri]:
                    rank.append(consultants[j]["name"])
                    # print(consultants[j]["name"])
        return rank

def book(consultants, hour, duration, criteria):
# your code here
    record=[]
    newBooking=[]
    cfmBooking=[]
#呼叫criteria決定的顧問排名
    rank("price",rankPrice)
    # print(rankPrice)
    rank("rate",rankRate)
    rankRate.sort(reverse=True)# rate要從大到小排名
    # print(rankRate)

    def checkTime(cri,rank): #cri="price"/"rate"; rank=rankPrice/rankRate
        if(criteria==cri):
            for i in rank:
                    newBooking=[i]+[(hour+x) for x in range(0,(duration+1))]
                    # print(newBooking)
                    for k in range(len(schedule)):
                        schedule[k][1:]=sorted(schedule[k][1:])
                        if(cfmBooking==[] and newBooking[0] in schedule[k]):
                            #1)檢查預約時間:不衝突→確認booking
                            # print("schedule=",schedule[k][1:])
                            # print("set_schedule=",set(schedule[k][1:]))
                            # print("Set_newBooking=",set(newBooking[1:]))
                            # print(set(newBooking[1:]) & set(schedule[k][1:]))
                            if set(newBooking[1:]) & set(schedule[k][1:])==set() :
                                    cfmBooking.extend(newBooking)
                                    schedule[k].extend(newBooking[1:])
                            else:
                                break      
        return cfmBooking, schedule
    def chooseRank(cri):
        if(cri=="price"):
             return rankPrice
        if(cri=="rate"):
             return rankRate
    
    checkTime(criteria,chooseRank(criteria))
    if(cfmBooking==[]):
         cfmBooking=["No Service"]  
    # print("cfm=",cfmBooking[0],"schedule=",schedule)
    print(cfmBooking[0])
consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]
print("-----------Task 2----------")
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John
#Task3
def func(*data):
# your code here
    # print(data)
    mid=[]
    count=0
    for n in range(0,len(data)):
        if len(data[n])==2:
            mid.append(data[n][1])
        elif len(data[n])==3:
            mid.append(data[n][1])
        elif len(data[n])==4:
            mid.append(data[n][2])
        elif len(data[n])==5:
            mid.append(data[n][2])
    # print("mid=",mid)    
    for n in range(0,len(mid)):
        if mid.count(mid[n])==1:
            print(data[n])
        else:
            count+=1
            if count==len(data): 
                print("沒有")
        
print("-----------Task 3----------")
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安
#Task4
def get_number(index):
# your code here
    result=0
    for i in range(index):
            # print("i=",i)
            if (i+1)%3!=0:
                result+=4
            elif (i+1)%3==0:
               result-=1
            # print(result)         
    print("index=",index,",","result =",result)
print("-----------Task 4----------")
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70