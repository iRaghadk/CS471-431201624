from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Count, Sum, Avg, Max, Min
from .models import Book, Publisher, Author, Student, Address, Student2, Address2, BookPhoto
from django.utils import timezone
from .forms import BookForm, StudentForm, Student2Form, BookPhotoForm

def index(request): 
    return render(request, "bookmodule/index.html") 
  
def list_books(request): 
    return render(request, 'bookmodule/list_books.html') 
  
def viewbook(request, bookId): 
    return render(request, 'bookmodule/one_book.html') 
  
def aboutus(request): 
    return render(request, 'bookmodule/aboutus.html')

# ==================== Lab 5 Views ====================
def links_view(request):
    return render(request, 'bookmodule/links.html')

def text_formatting_view(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing_view(request):
    return render(request, 'bookmodule/listing.html')

def tables_view(request):
    return render(request, 'bookmodule/tables.html')

# ==================== Lab 6 Views ====================
def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def search_view(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword')
        string = keyword.lower() if keyword else ""
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
                
        return render(request, 'bookmodule/bookList.html', {'books': newBooks})
        
    return render(request, 'bookmodule/search.html')

# Task 3: Simple Query
def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

# Task 4: Complex Query
def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]
    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')

# Lab 8 - Task 1
def lab8_task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Lab 8 - Task 2
def lab8_task2(request):
    books = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Lab 8 - Task 3
def lab8_task3(request):
    books = Book.objects.filter(~Q(edition__gt=3) & (~Q(title__icontains='qu') | ~Q(author__icontains='qu')))
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Lab 8 - Task 4
def lab8_task4(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books': books})

# Lab 8 - Task 5
def lab8_task5(request):
    aggregations = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/bookStats.html', {'aggregations': aggregations})

# Lab 8 - Task 7
#def student_city_count(request):
 #   cities = Address.objects.annotate(student_count=Count('student'))
  #  return render(request, 'bookmodule/studentCityCount.html', {'cities': cities})

# ==================== Lab 9 Views ====================

# Lab 9 - Task 1
def lab9_task1(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/bookAvailability.html', {'books': books})

# Lab 9 - Task 2
def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/publisherStock.html', {'publishers': publishers})

# Lab 9 - Task 3
def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_pubdate=Min('book__pubdate'))
    return render(request, 'bookmodule/oldestBookPublisher.html', {'publishers': publishers})

# Lab 9 - Task 4
def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/publisherPriceStats.html', {'publishers': publishers})

# Lab 9 - Task 5
def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_count=Count('book', filter=Q(book__rating__gte=4)),
        total_quantity=Sum('book__quantity')
    )
    return render(request, 'bookmodule/highRatedBooks.html', {'publishers': publishers})

# Lab 9 - Task 6 (Assignment Task)
def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_count=Count(
            'book',
            filter=Q(book__price__gt=50) & Q(book__quantity__lt=5) & Q(book__quantity__gte=1)
        )
    )
    return render(request, 'bookmodule/filteredBookCount.html', {'publishers': publishers})

# --- Lab 10: Part 1 ---
def lab10_part1_list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/list_books.html', {'books': books})

def lab10_part1_add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        Book.objects.create(
            title=title,
            price=price,
            quantity=quantity,
            pubdate=timezone.now()
        )
        return redirect('lab10_part1_list')
    return render(request, 'bookmodule/add_book.html')

def lab10_part1_edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.save()
        return redirect('lab10_part1_list')
    return render(request, 'bookmodule/edit_book.html', {'book': book})

def lab10_part1_delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('lab10_part1_list')


# --- Lab 10: Part 2 ---
def lab10_part2_list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_list_books.html', {'books': books})

def lab10_part2_add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.pubdate = timezone.now()
            book.save()
            return redirect('lab10_part2_list')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10_add_book.html', {'form': form})

def lab10_part2_edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab10_part2_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10_edit_book.html', {'form': form, 'book': book})

def lab10_part2_delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('lab10_part2_list')


# Lab 11 - Task 1: Student (ForeignKey)
def student_list(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/student_add.html', {'form': form})

def student_edit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/student_edit.html', {'form': form, 'student': student})

def student_delete(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect('student_list')

# Lab 11 - Task 2: Student2 (Many-to-Many)
def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/student2_list.html', {'students': students})

def student2_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/student2_add.html', {'form': form})

def student2_edit(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student2_list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/student2_edit.html', {'form': form, 'student': student})

def student2_delete(request, student_id):
    student = get_object_or_404(Student2, id=student_id)
    student.delete()
    return redirect('student2_list')

# Lab 11 - Task 3: BookPhoto (Image Upload)
def photo_list(request):
    photos = BookPhoto.objects.all()
    return render(request, 'bookmodule/photo_list.html', {'photos': photos})

def photo_add(request):
    if request.method == 'POST':
        form = BookPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = BookPhotoForm()
    return render(request, 'bookmodule/photo_add.html', {'form': form})

def photo_edit(request, photo_id):
    photo = get_object_or_404(BookPhoto, id=photo_id)
    if request.method == 'POST':
        form = BookPhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = BookPhotoForm(instance=photo)
    return render(request, 'bookmodule/photo_edit.html', {'form': form, 'photo': photo})

def photo_delete(request, photo_id):
    photo = get_object_or_404(BookPhoto, id=photo_id)
    photo.delete()
    return redirect('photo_list')