from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from hydrogen.visit_info import refresh_visitnumber,get_Userip

# Create your views here.
def todolist(request):
    refresh_visitnumber(request,'TodoList')
    return render(request, 'todolist/index.html')