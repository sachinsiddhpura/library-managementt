from django.db import models

# Create your models here.
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

User = settings.AUTH_USER_MODEL

class BookManager(models.Manager):
    def get_reference_book(self):
        return self.filter(category='referencebook')

    def get_text_book(self):
        return self.filter(category='textbook')

class Book(models.Model):
    CATEGORY_TYPE =(
        ('textbook','Text Book'),
        ('referencebook','Reference Book')
    )
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)
    category = models.CharField(max_length=120,choices=CATEGORY_TYPE)
    isbn = models.CharField(max_length=120,blank=True,null=True)

    objects = BookManager()

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('library:library_book_detail',args=[self.pk])
    
    def get_update_url(self):
        return reverse('library:library_book_update',args=[self.pk])

class Issue(models.Model):
    ISSUE_TYPE =(
        ('issued','Issued'),
        ('available','Available'),
        ('lost','Lost')
    )
    book = models.ForeignKey('Book',on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    shelf_id = models.CharField(max_length=120,blank=True,null=True)
    available_status = models.CharField(max_length=120,choices=ISSUE_TYPE)

    class Meta:
        verbose_name = _('Issue')
        verbose_name_plural = _('Issues')

    def __str__(self):
        return self.book.title

    def get_absolute_url(self):
        return reverse('library:library_issue_detail',args=[self.pk])
    
    def get_update_url(self):
        return reverse('library:library_issue_update',args=[self.pk])

class LogManager(models.Manager):
    def issued_between(self,from_date,to_date):
        return self.filter(date__range=[from_date,to_date])

    def by_issuer(self):
        return self.filter(category='textbook')

    def by_user(self,enrolment_number):
        return self.filter(user__enrolment_number=enrolment_number)

    def due_books(self):
        return self.filter(status='overdue')

    def pending_books(self):
        return self.filter(status='pending')

class Log(models.Model):
    STATUS_CHOICE = (
        ('pending','Pending'),
        ('returned','Returned'),
        ('over_due','Over_Due')
    )
    book_issue = models.ForeignKey('Issue',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='borrower', blank=True,null=True, on_delete=models.CASCADE)
    issued_by = models.ForeignKey(User,related_name='issuer', blank=True,null=True,on_delete=models.CASCADE)
    status = models.CharField(max_length=120,choices=STATUS_CHOICE,default='pending')
    issued_date = models.DateTimeField(auto_now_add=True)
    return_time = models.DateTimeField()
    fine = models.IntegerField(default=0)
    
    objects = LogManager()

    class Meta:
        verbose_name = _('Log')
        verbose_name_plural = _('Logs')

    def __str__(self):
        return self.book.shelf_id

    def get_absolute_url(self):
        return reverse('library:library_log_detail',args=[self.pk])
    
    def get_update_url(self):
        return reverse('library:library_log_update',args=[self.pk])