from django.shortcuts import render, redirect
from .forms import NewBlog
from .models import Blog
from django.contrib.auth.decorators import user_passes_test, login_required

# Create your views here.

def blogHome(request):
    allBlogs = Blog.objects.all()
    return render(request, "blog/blogHome.html", {"allBlogs": allBlogs})


# Add a new blog logic

def addBlog(request):
    if request.method == "POST":
        form = NewBlog(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blogHome")
    else:
            
        newForm = NewBlog()
    return render(request, "blog/addBlog.html", {'form': newForm})

def blogDetails(request, pk):
    blog = Blog.objects.get(pk = pk)
    return render(request, "blog/blogDetails.html", {"blog": blog} )

# a Blog detail login

def blogDetails(request, pk):
    blog = Blog.objects.get(pk = pk)
    return render(request, "blog/blogDetails.html", {"blog": blog} )

#  Create a delete function that delete a blog and redirect to home page

def is_admin(user):
    return user.is_superuser or user.is_staff

@user_passes_test(is_admin)
def deleteBlog(request, pk):
    blog = Blog.objects.get(pk = pk)
    if request.method == "POST":
        blog.delete()
        return redirect("blogHome")
    

# Adding a contact form for custormers to reach us
