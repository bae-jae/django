from django.shortcuts import render
from .models import BookInfo, Review,  Prob
from django.utils.dateparse import parse_date
from . import crawling
from django.utils import timezone
from . import dbCon
from .mbti import Mbti
import random

#def index(request):
#    return render(request, 'main.html')


def index(request):
    # userName = "배재"
    # fkModle = dbCon.getReadList("배재")
    
    fkModle = BookInfo.objects.all()
    
    context = {}
    
    title = []
    writer = []
    img = []
    review = []
    price = []
    mbti = []
    
    for i in fkModle:
        title.append(i.title)
        writer.append(i.writer)
        img.append(i.book_img)
        price.append(i.price)
        mbti.append(i.mbti)
        
        r = dbCon.getBookReview(i.title)
        
        if len(r) == 0:
            review.append('none')
        else:
            review.append(r[0].content)
    
    bookLink = "http://www.yes24.com/Product/Goods/"
    link = []
    
    html = crawling.getHtml('http://www.yes24.com/24/Category/BestSeller')
    bookInfo = crawling.getDetail(html)
    
    
    
    for i in bookInfo.keys():
        link.append(bookLink + bookInfo[i]['code'])
        
    context["bookInfo"] = zip(title, img, review, writer, price, mbti, link)
    context['Mbti'] = Mbti.MBTIDict.items()
    
    
    
    
    return render(request, "main.html", context)



def detailReview(request, bookName):
    reviewSet = dbCon.getBookReview(bookName)
    
    context ={}
    
    writer = []
    date = []
    review = []
    
    for r in reviewSet:
        writer.append(r.writer)
        review.append(r.content)
        date.append((str(r.date))[0:11])
        
    context['review'] = zip(writer, review, date)
     
    return render(request, "detailReview.html", context)
 


#책 정보와 user리뷰를 저장 인터넷에 읽어온 것만""""""
def store(request):
    html = crawling.getHtml('http://www.yes24.com/24/Category/BestSeller')
    bookInfo = crawling.getDetail(html)
    
    context = {}
    
    nameList = []
    imgList = []
    priceList = []
    writerList = []
    
    bookCode = []
    
    for i in bookInfo.keys():
        name = bookInfo[i]['name']
        src = bookInfo[i]['src']
        writer = bookInfo[i]['writer']
        price = bookInfo[i]['price']
        
        bookCode.append([name, bookInfo[i]['code']])
        
        try:
            book = BookInfo.objects.get(pk=name)
        except BookInfo.DoesNotExist:
            b = BookInfo(title = name, book_img = src, writer = writer, price= price, like_num= random.randint(0, 15), commnet_num= 0, mbti= Mbti.MBTI[random.randint(0, len(Mbti.MBTI) - 1)])
            b.save();
    
    print("Book 저장완료", len(bookCode))
    
    count = 0;
    
    for name, code in bookCode:
        review, writerInfo = crawling.getReview(code)      #2차원 배열   #느림\
        bookTable = BookInfo.objects.get(title = name)
        
        print(count, len(review), bookTable.title)
        count = count + 1
        
        if bookTable == None:
            print("책이 없다 ??")
        else:
            for idx, content in enumerate(review):
                try:
                    r = Review(title= bookTable, content= content, date= parse_date(writerInfo[idx][1]), writer= writerInfo[idx][0])
                    r.save();
                except:
                    print(writerInfo[idx][0], bookTable.title)
    
    return render(request, 'main.html')

