from django.contrib import admin

from .models import Category, Book, RentBook

class BookAdmin(admin.ModelAdmin):
    ordering = ["id"]
    model = Book
    list_display = ['title','category','author1','available_quantity']


class RentBookAdmin(admin.ModelAdmin):
    ordering = ["id"]
    model = RentBook
    list_display = ['member','book','rent_date','return_due_date','actual_return_date']


admin.site.register(Category)
admin.site.register(Book, BookAdmin)
admin.site.register(RentBook, RentBookAdmin)
