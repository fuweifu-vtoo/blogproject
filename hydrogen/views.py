from django.shortcuts import render

# Create your views here.
def hydrogen(request):
    return render(request, 'hydrogen/index.html')
