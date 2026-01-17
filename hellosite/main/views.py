from django.shortcuts import render

def hello_view(request):
    """
    View to render a single page with the text 'Hello!'.
    """
    return render(request, 'main/hello.html')
