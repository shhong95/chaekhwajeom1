from django.contrib import admin
from .models import Book, Review, Comment
from .forms import ReviewForm

# Register your models here.
admin.site.register(Book)
admin.site.register(Comment)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm 