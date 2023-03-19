from django.shortcuts import render

# Create your views here.
def index(request):
    # Your view logic here
    context = {}
    if request.user.is_authenticated:
        context['is_authenticated'] = True
    
    return render(request, 'index.html',context)