from django.shortcuts import render

def about(request):

    return render(request, 'appTemp/about/about.html')