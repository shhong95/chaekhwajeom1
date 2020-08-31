from django.contrib import admin
from .models import Book, Review
from .forms import ReviewForm

# Register your models here.
admin.site.register(Book)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    form = ReviewForm 