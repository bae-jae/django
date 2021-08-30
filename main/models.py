from django.db import models


class BookInfo(models.Model):
    title = models.CharField(primary_key = True, max_length = 30)              #한글 
    book_img = models.ImageField(blank=True, null=True)                        #이미지 소스
    writer = models.CharField(max_length=20)                                   #저자
    price = models.CharField(max_length=20)                                    #가격
    mbti = models.CharField(max_length=4)                                      #mbti 매충
    like_num = models.IntegerField()                                             
    commnet_num = models.IntegerField()  

    def __str__(self):
        return self.title

class Review(models.Model):
    title = models.ForeignKey(BookInfo, on_delete=models.CASCADE, db_column = "title") #post의 아이디를 참조  #db_colume 설정 필요 
    content = models.TextField()
    writer = models.CharField(max_length=20)
    date = models.DateTimeField()                                              #언제 입력됐는지?

    def __str__(self):
        return self.content
    
    class Meta:
        unique_together = (("title", "writer"))                        #한사람당 책에 하나의 리뷰만 작성


class User(models.Model):
    id = models.CharField(max_length=20, primary_key = True)                          #사용자 id 
    point = models.IntegerField()
    mbti = models.CharField(max_length=4)
    
    def __str__(self):
        return self.id
        
class Read(models.Model):                                                                  #db이름 수정 필요하
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column = "user_id")     #post의 아이디를 참조  #db_colume 설정 필요
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, db_column = "book")
    is_finish = models.IntegerField()                                                      #문제 풀었나
    is_onGoing = models.IntegerField()                                                     #책 진행도
    is_reviewed = models.IntegerField()                                                    #리뷰 적었나?
    
    
    def __str__(self):
        return "%s %s" % (self.user_id, self.book)
    
    class Meta:
        unique_together = (("user_id", "book"))
        
class Prob(models.Model):                                                                  
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column = "user_id")     #출제자 
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, db_column = "book")       #책이름
    prob1 = models.TextField()                                                             #문제 풀었나
    prob2 = models.TextField()                                                             #문제 풀었나
    prob3 = models.TextField()                                                             #문제 풀었나
    
    answer = models.TextField()                                                            #정답

    def __str__(self):
        return "%s %s" % (self.user_id, self.book)
