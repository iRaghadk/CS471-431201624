from django import forms
from .models import Book, Student, Address, Student2, Address2, BookPhoto

# --- Lab 10 ---
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity']

# --- Lab 11 - Task 1 ---
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

# --- Lab 11 - Task 2 ---
class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple(),
        }

# --- Lab 11 - Task 3 ---
class BookPhotoForm(forms.ModelForm):
    class Meta:
        model = BookPhoto
        fields = ['title', 'image']