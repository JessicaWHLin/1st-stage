<<<<<<< HEAD
import urllib.request as req
import bs4
import csv
finalResult=[]
def subPageDate(subPage): #爬子頁的網頁，找日期時間
    request=req.Request(subPage,headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data2=response.read().decode("utf-8")
  
    root=bs4.BeautifulSoup(data2,"html.parser")
    articles=root.find_all("span",class_="article-meta-value")
    if articles != []:
        return articles[-1].string
    else:
        return " "

def getData(url):
    request=req.Request(url,headers={
        "cookie":"over18=1", #增加cookie:已滿18歲
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response: 
        data=response.read().decode("utf-8")
    #解析原始碼，取得每篇文章
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    like_counts=root.find_all("div",class_="nrec")
    sameTitleLink=[]
    # 印出結果   
    for i in range(len(titles)):
        if titles[i].a !=None: #如果標題包含a標籤(沒有被刪除)印出來
            subPages=root.find_all("a",string=titles[i].a.string) #找到內文是"文章標題"的a標籤，抓子頁的網址
            #當同一頁碰到一樣的文章題目時，要判斷
            subPage=None
            while subPage==None:
                for j in range(0,len(subPages)):
                    if subPages[j] not in sameTitleLink:
                        subPage="https://www.ptt.cc/"+subPages[j]["href"]
                        sameTitleLink.append(subPages[j])
                        break
                    else: 
                        continue
                        
            if like_counts[i].string !=None:
                finalResult.append([titles[i].a.string,like_counts[i].string,subPageDate(subPage)])
                print(titles[i].a.string,like_counts[i].string,subPageDate(subPage))
            else:
                finalResult.append([titles[i].a.string," ",subPageDate(subPage)])
                print(titles[i].a.string," ",subPageDate(subPage))
         
    # # 抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的a標籤
    return nextLink["href"]

#主程式:抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc/"+getData(pageURL)
    count+=1

#把結果寫入csv檔案
with open("article.csv", mode="w", newline="",encoding="utf-8-sig") as file:
    writer=csv.writer(file)
    for i in range(len(finalResult)):
        writer.writerow(finalResult[i])
    
=======
import urllib.request as req
import bs4
import csv
finalResult=[]
def subPageDate(subPage): #爬子頁的網頁，找日期時間
    request=req.Request(subPage,headers={
    "cookie":"over18=1",
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response:
        data2=response.read().decode("utf-8")
  
    root=bs4.BeautifulSoup(data2,"html.parser")
    articles=root.find_all("span",class_="article-meta-value")
    if articles != []:
        return articles[-1].string
    else:
        return " "

def getData(url):
    request=req.Request(url,headers={
        "cookie":"over18=1", #增加cookie:已滿18歲
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36"
    })
    with req.urlopen(request) as response: 
        data=response.read().decode("utf-8")
    #解析原始碼，取得每篇文章
    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title")
    like_counts=root.find_all("div",class_="nrec")
    sameTitleLink=[]
    # 印出結果   
    for i in range(len(titles)):
        if titles[i].a !=None: #如果標題包含a標籤(沒有被刪除)印出來
            subPages=root.find_all("a",string=titles[i].a.string) #找到內文是"文章標題"的a標籤，抓子頁的網址
            #當同一頁碰到一樣的文章題目時，要判斷
            subPage=None
            while subPage==None:
                for j in range(0,len(subPages)):
                    if subPages[j] not in sameTitleLink:
                        subPage="https://www.ptt.cc/"+subPages[j]["href"]
                        sameTitleLink.append(subPages[j])
                        break
                    else: 
                        continue
                        
            if like_counts[i].string !=None:
                finalResult.append([titles[i].a.string,like_counts[i].string,subPageDate(subPage)])
                print(titles[i].a.string,like_counts[i].string,subPageDate(subPage))
            else:
                finalResult.append([titles[i].a.string," ",subPageDate(subPage)])
                print(titles[i].a.string," ",subPageDate(subPage))
         
    # # 抓取上一頁的連結
    nextLink=root.find("a",string="‹ 上頁") #找到內文是‹ 上頁的a標籤
    return nextLink["href"]

#主程式:抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Lottery/index.html"
count=0
while count<3:
    pageURL="https://www.ptt.cc/"+getData(pageURL)
    count+=1

#把結果寫入csv檔案
with open("article.csv", mode="w", newline="",encoding="utf-8-sig") as file:
    writer=csv.writer(file)
    for i in range(len(finalResult)):
        writer.writerow(finalResult[i])
    
>>>>>>> cd20fd2c52ddac3f93d9be333314110c992b65e5
    