from django.shortcuts import render

# Create your views here.

def api_view(request):

    return render(request, 'api/principal.html')