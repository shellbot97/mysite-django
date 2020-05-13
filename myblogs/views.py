from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    blogs = Blog.objects.filter(user=request.user, is_active=True)
    return render(request, 'index.html', {
        'blogs': blogs,
    })


@login_required(login_url='/accounts/login')
def create_blog(request):
    form = BlogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        blog.img = request.FILES['img']
        file_type = blog.img.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'album': blog,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            return render(request, 'create_blog.html', context)
        blog.save()
        return redirect('blogs:index')
    context = {
        "form": form,
    }
    return render(request, 'create_blog.html', context)
