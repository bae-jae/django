from django.shortcuts import render
from .models import Mention
import csv

# Create your views here.


def index(request):
    return render(request, 'premain.html')


def bulk_import(request):
    CSV_PATH = '/workspace/BOOK/static/mention_list.xlsx'

    with open(CSV_PATH, newline='', encoding='euc-kr') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            Wifi.objects.create(
                title=row['제목'],
                content=row['내용'],
                writer=row['저자'],
            )
    return