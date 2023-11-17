from django.shortcuts import render

# Create your views here.
def deck_list(request):
    return render(request, 'deck_list.html')
