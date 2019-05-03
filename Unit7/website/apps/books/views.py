from django.shortcuts import render, redirect, get_object_or_404
from apps.books.models import Book
from apps.books.form import BookForm


# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request, template_name='index.html', context={'books': books})


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()
    return render(request, template_name='create-book.html', context={'form': form})


def update_book(request, pk):
    # Don't do this
    # book = Book.objects.get(pk=int(pk))
    # print(book)
    book = get_object_or_404(Book, pk=int(pk))

    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name='update-book.html', context={'form': form})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=int(pk))
    book.delete()
    return redirect('/')
