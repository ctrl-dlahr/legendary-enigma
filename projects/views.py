from django.shortcuts import render

# Create your views here.
def index(request):
    """List all projects."""
    return render(request, 'index.html')