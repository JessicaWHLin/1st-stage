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
