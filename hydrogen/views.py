from django.shortcuts import render

# Create your views here.
def hydrogen(request):
    return render(request, 'hydrogen/index.html')
    
def contact(request):
    return render(request, 'hydrogen/contact.html')

def about(request):
    return render(request, 'hydrogen/about.html')