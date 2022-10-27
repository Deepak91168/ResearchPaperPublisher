import site
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.utils import timezone
from home.models import Posts, Category
from django.contrib.auth.forms import UserCreationForm


def home(request):
    papers = Posts.objects.all().order_by('-post_time')
    categories = Category.objects.all()
    recent_posts = Posts.objects.all().order_by('-post_time')
    paper_Data = {
        'papers': papers,
        'categories': categories,
        'recent_posts': recent_posts
    }
    if request.user.is_authenticated:
        return render(request, 'turnup/index.html', paper_Data)
    else:
        return redirect('account_login')


def about(request):
    categories = Category.objects.all()
    return render(request, 'turnup/about.html', {'categories': categories})


def paper(request, url):
    single_post = Posts.objects.get(url=url)
    related_posts = Posts.objects.filter(cat=single_post.cat).exclude(url=url)
    categories = Category.objects.all()

    return render(
        request, 'turnup/paper.html', {
            'single_post': single_post,
            'categories': categories,
            'related_posts': related_posts
        })


def category(request, url):
    cat = Category.objects.get(url=url)
    categories = Category.objects.all()
    posts = Posts.objects.filter(cat=cat)
    return render(request, 'turnup/categoy.html', {
        'cat': cat,
        'categories': categories,
        'posts': posts
    })


def categorypage(request):
    categories = Category.objects.all()
    papers = Posts.objects.all()
    cat_Data = {'papers': papers, 'categories': categories}
    return render(request, 'turnup/allcategory.html', cat_Data)
