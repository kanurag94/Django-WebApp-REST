from django.shortcuts import render

posts = [
    {
        'author':'anurag',
        'title' : 'something',
        'content':'Soemthing is beautiful',
        'date': 'August 12, 2019'
    },
    {
        'author':'anurag2',
        'title' : 'something2',
        'content':'Soemthing is beautiful2',
        'date': 'August 12, 20192'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Page'})