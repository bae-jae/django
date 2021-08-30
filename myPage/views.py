from django.shortcuts import render, redirect
from main import dbCon
from main.models import Review, BookInfo, User, Prob
from django.utils import timezone


def index(request):
    userName = "배재"
    fkModle = dbCon.getReadList(userName)        #내가 읽은 책 목록 반환
    
    context = {}
    
    title = []            
    img = []
    review = []                                    # -> "내가 쓴 리뷰만 보여줌"
    date = []
    mbti = []
    writer = []
    reviewLen = []
    
    for i in fkModle:
        img.append(i.book.book_img)
        title.append(i.book.title)
        writer.append(i.book.writer)
        mbti.append(i.book.mbti)
        
        print("읽은 책", i.book.title)
        
        try:
            r = dbCon.getBookReviewByUserName(userName, i.book)
            review.append(r.content)
            date.append((str(r.date))[0:11])
        except:
            review.append('리뷰를 작성해주세요')
            date.append('')

    context = { "bookInfo" : zip(title, img, review, date)}
        
    context["bookInfo"] = zip(title, img, review, date, writer, mbti) 
    context["name"] = userName
    context["reviewLen"] = len(review)
    
    #리뷰 문제를 뽑는 장소
    storeprob = []
    
    answer = []
    
    for i in fkModle:
        try:
            p = Prob.objects.filter(book = i.book)
            p[0]
            for probList in p:
                prob = []
                prob.append(i.book.title)
                prob.append(probList.prob1)
                prob.append(probList.prob2)
                prob.append(probList.prob3)
                prob.append(probList.answer)
                
                storeprob.append(prob)
        except:
            prob = []
            prob.append(i.book.title)
            prob.append("문제 출제 필요")
            prob.append("문제 출제 필요")
            prob.append("문제 출제 필요")
            prob.append("1111")
                
            storeprob.append(prob)
            
    context['probList'] = storeprob
    return render(request, "myPage.html", context)



def detailReview(request, bookName):
    print("디테일 뷰" + bookName)
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

  
def store(request, user):
    title = request.POST.get('bookName')
    review = request.POST.get('review')
    title = BookInfo.objects.get(title=title)
    
    try:
        r = Review(title= title, content= review, date= timezone.now(), writer= user)
        r.save()
    except:
        Review.objects.filter(writer= user, title= title).update(content=review)
        
    print(title, review)
    return redirect('myPage:index')


def storeprob(request, user):
    title = request.POST.get('title')
    
    print("title")
    title = BookInfo.objects.get(title=title)
    user = User.objects.get(id = user)
    
    prob1 = request.POST.get('prob0')
    prob2 = request.POST.get('prob1')
    prob3 = request.POST.get('prob2')
    
    
    answer = request.POST.get('mprob0') + request.POST.get('mprob1') +                  request.POST.get('mprob2') 
    
    r = Prob(book= title, user_id = user, prob1 = prob1, prob2 = prob2, prob3 = prob3,
                answer = answer)
    r.save()
        
    print("성공")
    return redirect('myPage:index')
    
    