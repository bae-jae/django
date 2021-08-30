from .models import Review, BookInfo, User, Read

def getBookReview(title):
    Model =  BookInfo.objects.get(title = title)
    
    return Model.review_set.all()

def getBookReviewByUserName(user, title):
    return Review.objects.get(writer= user, title= title)
        
def getReadList(user_id):
    user =  User.objects.get(id = user_id)
    return  Read.objects.filter(user_id = user)        #queryset반환


