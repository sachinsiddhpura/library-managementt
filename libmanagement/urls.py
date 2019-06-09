from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('library/log_book/',views.log_book,name='log_book'),
    path('library/return_book/',views.return_book,name='return_book'),
    path('library/return_book_handler/',views.return_book_handler,name='return_book_handler'),
    path('',views.index,name='index'),

    path('library/book/', views.BookListView.as_view(), name='library_book_list'),
    path('library/book/create/', views.BookCreateView.as_view(), name='library_book_create'),
    path('library/book/detail/<int:pk>/', views.BookDetailView.as_view(), name='library_book_detail'),
    path('library/book/update/<int:pk>/', views.BookUpdateView.as_view(), name='library_book_update'),

    path('library/issue/', views.IssueListView.as_view(), name='library_issue_list'),
    path('library/issue/create/', views.IssueCreateView.as_view(), name='library_issue_create'),
    path('library/issue/detail/<int:pk>/', views.IssueDetailView.as_view(), name='library_issue_detail'),
    path('library/issue/update/<int:pk>/', views.IssueUpdateView.as_view(), name='library_issue_update'),

    path('library/log/', views.LogListView.as_view(), name='library_log_list'),
    path('library/log/create/', views.LogCreateView.as_view(), name='library_log_create'),
    path('library/log/detail/<int:pk>/', views.LogDetailView.as_view(), name='library_log_detail'),
    path('library/log/update/<int:pk>/', views.LogUpdateView.as_view(), name='library_log_update'),
]