from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def file_path(instance,filename):
    extension = filename.split('.')[-1]
    isbn=instance.ISBN

    return 'covers/%s.%s' %(isbn,extension)

# Create your models here.
class Book(models.Model):

    STATUS_CHOICES = (
        ('대여가능','대여 가능'),
        ('예약','예약 중'),
        ('대여중','대여 중'),
        ('대여불가능','대여 불가능'),
    )

    ISBN = models.CharField(max_length=13,unique=True)
    title = models.CharField('도서명',max_length=30)
    author = models.CharField('저자',max_length=30, blank=True)
    publisher = models.CharField('출판사',max_length=30,blank=True)
    intro = models.TextField('서평',max_length=100)
    status = models.CharField('상태',max_length=10,choices=STATUS_CHOICES,default='대여가능')
    bookcover = ProcessedImageField(
        upload_to=file_path,
        processors=[ResizeToFill(480,640)],
        options={'quality':90},
        blank=True)
    stored_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-stored_at']

    def __str__(self):
        return self.title 


class Review(models.Model):
    book = models.OneToOneField(Book,on_delete=models.CASCADE,primary_key=True)
    book_review=models.TextField('리뷰',max_length=100)
    rate=models.IntegerField(
        '별점',
        validators=[MinValueValidator(1),MaxValueValidator(5)],
        default=1)


class Comment(models.Model):
    objects = models.Manager()
    post = models.ForeignKey('Review', on_delete=models.CASCADE)
    text = models.TextField(default='')
    created_date = models.DateTimeField(default=timezone.now)
