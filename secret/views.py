from django.shortcuts import render

# Create your views here.
def secret_page(request):
    stuffs = {}
    return render(request,
                  'secret/index.html',
                  {'data':stuffs})
