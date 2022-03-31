from django.shortcuts import render
from django.http.response import HttpResponse

def index_template(request):
    myapp_data = {
      'app': 'Django'
    }
    return render(request, 'index.html', myapp_data)