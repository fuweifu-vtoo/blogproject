from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from hydrogen.visit_info import refresh_visitnumber,get_Userip
from hydrogen.models import VisitNumber

# Create your views here.
def todolist(request):
    refresh_visitnumber(request,'TodoList')
    TodoList_visit_nums = VisitNumber.objects.filter(page_name='TodoList')
    TodoList_count_nums = TodoList_visit_nums[0]
    nums = TodoList_count_nums.count + 327

    return render(request, 'todolist/index.html',context={'nums': nums})
