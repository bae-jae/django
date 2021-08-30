from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re

def getHtml(url):
    page_html = urlopen(url)
    bsObject = BeautifulSoup(page_html, "html.parser")
    
    return bsObject

def getCutIdx(string, target, it):
    count = 0
    idx = 0
    
    for i in range(len(string)):
        if string[i] == target:
            count += 1
            idx = i;
            
        if it == count:
            break;
            
    return idx + 1
        

def getDetail(html):
    result = html.find('div', {'id': 'bestList'})
    result = result.select("ol > li")
    
    #내용도 dict로 변경 
    yes24BookInfo = {}
    
    for items in result:
        item = items.select("p")
        name = ''
        bookInfo = {}
        
        for idx, val in enumerate(item):
            if idx == 1:            #img src 
                bookInfo['src'] = val.a.img['src']
                
            if idx == 2:
                name = val.a.text                #책이름
                cutidx = getCutIdx(val.a['href'], '/', 3)    #책번호
                code = val.a['href'][cutidx:]
                
                bookInfo['name'] =  name;
                bookInfo['code'] =  code;
                
            if idx == 3:
                writer = val.a.text                #작가
                bookInfo['writer'] =  writer;
                
            if idx == 4:
                price = val.strong.text
                bookInfo['price'] =  price;
                break;
                
        yes24BookInfo[name] = bookInfo
    
    print("완료")    
    return yes24BookInfo
        
    
#http://www.yes24.com/Product/CommunityModules/GoodsReviewList/
#url 고정
def getReview(bookCode):
    url = 'http://www.yes24.com/Product/CommunityModules/GoodsReviewList/'
    html = getHtml(url + bookCode)

    result = html.select('div.reviewInfoGrp')
    
    review = []
    writerInfo = []
    
    for idx, item in enumerate(result):
        r = str(item.select("div.origin")[0].select("div.review_cont")[0])     #innerHTML로 넣을 거 여서 리뷰 원문을 뽑음 
        writer = item.select("a.lnk_id")[0].text
        date = item.select("em.txt_date")[0].text
        
        review.append(r)
        writerInfo.append([writer, date])
        
            
                                            #쓴 사람이랑 날짜
    
    # print(review[0])
    # print(writerInfo[0])   
    return review, writerInfo
                
# html = getHtml("http://www.yes24.com/24/Category/BestSeller")
# getDetail(html)
# http://www.yes24.com/Product/CommunityModules/GoodsReviewList/102789938
# getReview("102789938")
