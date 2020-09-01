from django import forms
from .models import Book, Review, Comment
from .widgets import starWidget

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        widgets = {
            'rate': starWidget,
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]