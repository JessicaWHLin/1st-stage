# your code here, maybe
schedule=[]
def book(consultants, hour, duration, criteria):
# your code here
    record=[]#被判斷的內容
    newBooking=[]
    con=[]
    for i in range(0,len(consultants)):
            con.append(consultants[i]["name"]) #確認顧問名字

    for i in range(0,len(consultants)): #按照criteria排序紀錄記錄在record
        # print(i)
        for key, value in consultants[i].items():
            if criteria ==key:
                record.append(value)
        if criteria=="price":#價錢由小到大
            record.sort()
        else:#其他criteria由大到小
              record.sort(reverse=True)        
    # print(record[0])

    for i in range(0,len(consultants)):#找到最佳的顧問
        for key, value in consultants[i].items():
            if record[0]== value:
                newBooking=[consultants[i]["name"]]+[(hour+x) for x in range(0,(duration+1))]#紀錄被booking顧問的起始時間
                # print("i=",i,"newBooking=",newBooking)
                # print(schedule)
    
    if schedule==[]:
        schedule.append(newBooking)
        print(newBooking[0])
    else:
        for i in range(len(schedule)):
            if  newBooking[0] not in schedule[i] and newBooking[0] in con:
                continue
            elif newBooking[0] in schedule[i]: #如果顧問已在預約表中:做判斷
                # print("進判斷1",schedule)
                #1)檢查預約時間:不衝突→加入booking
                if newBooking[1] not in schedule[i][1:] and newBooking[-1] not in schedule[i][1:]:
                    # print(schedule[i])
                    schedule[i]+=newBooking[1:]
                    print(newBooking[0])
                else:#2)衝突:重找
                    print("進判斷2")
                    for j in range(0,len(consultants)):
                        for key, value in consultants[j].items():
                            if record[1]==value:
                                    newBooking=[consultants[j]["name"]]+[(hour+x) for x in range(0,(duration+1))]
                    if newBooking[0] not in schedule[0][0]:
                        schedule.append(newBooking) 
                        print(newBooking[0],"次好")
                    else:
                        for j in range(0,len(consultants)):
                            for key, value in consultants[j].items():
                                if record[2]==value:
                                    newBooking=[consultants[j]["name"]]+[(hour+x) for x in range(0,(duration+1))]
                        schedule.append(newBooking)
                        print(newBooking[0],"最後")
  
    # print(schedule)      


consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]
# print("-----------Task 2----------")
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John