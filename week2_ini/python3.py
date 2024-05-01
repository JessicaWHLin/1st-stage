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