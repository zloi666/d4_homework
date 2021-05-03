from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from library.models import Book, Author, Publisher

def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)


def index(request):
    template = loader.get_template("index.html")
    books = Book.objects.all()
    data = {"title": "мою библиотеку",
            "books": books
            }

    return HttpResponse(template.render(data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def publisher(request):
    # template = loader.get_template("publisher.html")
    # books = Book.objects.all()
    # data = {"books": books}

    # return HttpResponse(template.render(data, request))

    template = loader.get_template("publisher.html")
    publishers = Publisher.objects.all()
    data = {
        "publishers": publishers
    }
    return HttpResponse(template.render(data, request))
