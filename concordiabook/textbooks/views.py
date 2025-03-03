from django.shortcuts import render
from .models import Textbook

# Create your views here.
def textbook_list(request, course_code):
    textbooks = Textbook.objects.filter(course_code=course_code, available=True)
    return render(request, 'textbooks/textbook_list.html', {'textbooks': textbooks, 'course_code': course_code})