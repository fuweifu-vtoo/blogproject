from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# Create your views here.
def todolist(request):
    return render(request, 'todolist/index.html')