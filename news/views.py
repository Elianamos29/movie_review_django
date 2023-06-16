from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss': newss})