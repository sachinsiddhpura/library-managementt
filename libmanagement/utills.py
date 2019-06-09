from libmanagement.models import Book,Log,Issue

def has_due(enrolment_number):
    logs = Log.objects.by_user(enrolment_number)
    due_books = list()
    for log in logs:
        if log.status == 'over_due':
            due_books.append(log)
    if len(due_books) == 0:
        return False,due_books
    else:
        return True,due_books