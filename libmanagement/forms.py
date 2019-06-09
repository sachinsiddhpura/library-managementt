from django import forms
from .models import Book, Issue, Log


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'category', 'isbn']


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['shelf_id', 'available_status', 'book', 'user']


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['return_time', 'book_issue', 'user', 'issued_by']
