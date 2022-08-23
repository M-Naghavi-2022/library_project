import datetime

from django.utils import timezone
from django.db import models

from user_app.models import MemberProfile


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    subject1 = models.CharField(max_length=100, null=True, blank=True)
    subject2 = models.CharField(max_length=100, null=True, blank=True)
    subject3 = models.CharField(max_length=100, null=True, blank=True)
    author1 = models.CharField(max_length=255)
    author2 = models.CharField(max_length=255, null=True, blank=True)
    author3 = models.CharField(max_length=255, null=True, blank=True)
    is_translated = models.BooleanField()
    translator1 = models.CharField(max_length=255, null=True, blank=True)
    translator2 = models.CharField(max_length=255, null=True, blank=True)
    translator3 = models.CharField(max_length=255, null=True, blank=True)
    publisher = models.CharField(max_length=255)
    publish_year = models.CharField(max_length=4)
    total_quantity = models.SmallIntegerField()
    available_quantity = models.SmallIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="books_photos/", default="default_book.png")

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.available_quantity is None:
            self.available_quantity = self.total_quantity
        if self.available_quantity > self.total_quantity:
            raise Exception("available_quantity can not be greater than total_quantity")
        return super().save(*args, **kwargs)


class RentBook(models.Model):
    member = models.ForeignKey(MemberProfile, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    rent_date = models.DateField(auto_now_add=True)
    return_due_date = models.DateField(null=True,blank=True)
    actual_return_date = models.DateField(null=True,blank=True)

    def save(self, *args, **kwargs): 
        if self.return_due_date is None:
            self.return_due_date = timezone.now().date() + datetime.timedelta(days=20)
            self.book.available_quantity -= 1
            self.book.save()
        if self.actual_return_date is not None:
            self.book.available_quantity += 1
            self.book.save()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.member.username} / {self.book.title}"