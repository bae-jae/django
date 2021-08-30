from django.contrib import admin
from .models import BookInfo, Review,User, Read, Prob

admin.site.register(BookInfo)
admin.site.register(Review)
admin.site.register(User)
admin.site.register(Read)
admin.site.register(Prob)