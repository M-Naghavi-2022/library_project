from functools import reduce
from operator import or_

from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from . models import Book


class BookList(LoginRequiredMixin, View):
    
    login_url = '/login/'
    redirect_field_name = 'next'
    def get(self, request):
        
        books = Book.objects.all()

        f = request.GET.get("filtered_category")
        if f:
            books = books.filter(category__name = f)
        
        search_fields = [
            'title',
            'subject1','subject2','subject3',
            'author1','author2','author3',
            'translator1','translator2','translator3',
            'publisher'
        ]

        search = request.GET.get("search")
        if search:
            q = reduce(or_, [Q(**{f'{f}__contains': search}) for f in search_fields], Q())
            books = books.filter(q)
        
        categories = {}
        for book in books:
            if book.category.name not in categories:
                categories.setdefault(book.category.name, [])
            categories[book.category.name].append(book)
        
        context = {
            'categories': categories
        }
        return render(request, 'book/book-list.html', context)

