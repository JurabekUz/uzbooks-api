from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(BookSource)
admin.site.register(BookReview)
