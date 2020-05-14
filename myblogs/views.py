from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
import csv, io

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


# Create your views here.
@login_required(login_url='/accounts/login')
def index(request):
    blogs = Blog.objects.filter(user=request.user, is_active=True)

    query = request.GET.get("q")
    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()

    page = request.GET.get('page', 1)
    paginator = Paginator(blogs, 5)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {
        'blogs': blogs,
    })


@login_required(login_url='/accounts/login')
def create_blog(request):
    form = BlogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        if len(request.FILES) != 0:
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
        blog.title = form.cleaned_data['title']
        blog.description = form.cleaned_data['description']
        blog.content = form.cleaned_data['content']
        blog.save()
        return redirect('blogs:index')
    context = {
        "form": form,
    }
    return render(request, 'create_blog.html', context)


@login_required(login_url='/accounts/login')
def detail(request, blog_id):
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog': blog, 'user': user})


@login_required(login_url='/accounts/login')
def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    user = request.user
    form = BlogForm(request.POST or None, request.FILES or None, instance=blog)

    if form.is_valid():
        blog = form.save(commit=False)
        blog.user = request.user
        if len(request.FILES) != 0:
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
        blog.title = form.cleaned_data['title']
        blog.description = form.cleaned_data['description']
        blog.content = form.cleaned_data['content']
        blog.save()
        return redirect('blogs:index')

    return render(request, 'update_blog.html', {'form': form, 'user': user})


@login_required(login_url='/accounts/login')
def delete(request, blog_id):
    user = request.user
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.is_active = False
    blog.save()
    return redirect('blogs:index')


@login_required(login_url='/accounts/login')
def bulk_create_blog(request):
    csv_file = request.FILES['file']

    if csv_file.name.endswith('.csv'):
        HttpResponse("not csv file")

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Blog.objects.update_or_create(
            title=column[0],
            description=column[1],
            content=column[2],
        )
    return redirect('blogs:index')