from django.shortcuts import render

# Create your views here.
from search.search import PostDocument


def search(request):
    q = request.GET.get('q')

    if q:
        posts = PostDocument.search().query("match", title=q)
    else:
        posts = ''

    return render(request, 'search.html', {'posts': posts})