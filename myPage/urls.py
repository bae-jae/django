from django.urls import path
from . import views

app_name = 'myPage'

urlpatterns = [
    path('', views.index, name='index'),                                   #일단 간단한 사람으로 테스트
    path("<str:bookName>/", views.detailReview, name="detailReview"),        #상세 리뷰페이지로 
    path("store/<str:user>/", views.store, name="store"),
    path("probstore/<str:user>/", views.storeprob, name="storeprob"),
]
