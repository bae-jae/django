import requests
from bs4 import BeautifulSoup


def book_recommend():
    book_img = []
    book_title = []

    url = "http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79"
    res = requests.get(url)
    xml = res.text
    soup = BeautifulSoup(xml, 'html.parser')
    book_list = soup.find('div', id = "main_contents").findAll('li')
        for i in book_list:
            book_img.append(i.find('div', class = "cover").img)
            
        for i in book_list:
            book_title.append(i.find('div', class = "title").text)
            
    return book_img, book_title