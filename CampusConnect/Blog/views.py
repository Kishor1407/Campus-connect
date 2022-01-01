from django.shortcuts import redirect, render
from .models import Blogpost
from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime
from django.contrib import messages


def home(request):
    blog = Blogpost.objects.all()
    return render(request, 'blog/home.html', {'blog': blog})


def editor(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    print(post.content)
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if request.FILES.get("banner"):
            image = request.FILES.get("banner")
            post.Banner_image=image
        post.title=title
        post.content=content
        post.pub_date=datetime.datetime.now()
        print(post.title)
        post.save()
        return redirect("/blog/dashboard")
    return render(request, 'blog/editor.html',{"post":post})

def write(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST.get("title")
            content = request.POST.get("content")
            image = request.FILES.get("banner")
            blog =Blogpost(
                user=request.user,
                title=title,
                content=content,
                pub_date=datetime.datetime.now(),
                Banner_image=image,
            )
            blog.save()
        return render(request, 'blog/write.html')
    else:
        messages.error(request, "Login to continue")
        return redirect("/login")

def blog(request, id):
    post = Blogpost.objects.filter(post_id=id)[0]
    try:
        more = Blogpost.objects.filter(post_id=(id+1))[0]
        return render(request, 'blog/blog.html', {'post': post, 'more': more})
    except IndexError:
        return render(request, 'blog/blog.html', {'post': post})


def dashboard(request):
    if request.user.is_authenticated:
        post = Blogpost.objects.filter(user=request.user)
        return render(request, 'blog/dashboard.html',{"post":post})
    else:
        return HttpResponse("404-page not found")


def delete(request,id):
    post = Blogpost.objects.filter(post_id=id)[0]
    post.delete()
    return redirect("/blogs/dashboard")