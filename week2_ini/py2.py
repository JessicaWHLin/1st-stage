# your code here, maybe
schedule=[]
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
def ini_schedule(con,sch):
    for i in range(0,len(con)):
        # for key in con[i].items():
            sch.append([con[i]["name"]])
    # print(sch)
    return sch

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
    # print(schedule==[])
    if(schedule==[]):
        ini_schedule(consultants,schedule)
        print(schedule)
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