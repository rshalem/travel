from blog.models import Article
from blog.forms import BlogCreate
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required



def index(request):
    all_article = Article.objects.all().order_by('-date_published')
    return render(request, 'blog/index.html', {'all_article': all_article})


def blog_detail(request, slug):
    single_blog = Article.objects.get(slug=slug)
    return render(request, 'blog/blog_detail.html', {'single_blog': single_blog})

# this decorator requires login in order to edit, login url takes you to required url, here Login view
@login_required(login_url="/login/")
def create_blog(request):
    if request.method == 'POST':
        form = BlogCreate(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('blog:index')
        else:
            messages.info(request, 'Invalid Entry')
            return redirect('blog:create_blog')
    else:
        form = BlogCreate()

    return render(request, 'blog/blog_create.html', {'form': form})


# def create_blog(request):
#     if request.method == 'POST':
#
#         form = BlogCreate(request.POST)
#
#         if form.is_valid():
#
#             title = form.cleaned_data['title']
#             author = form.cleaned_data['author']
#             content = form.cleaned_data['content']
#             date = form.cleaned_data['date']
#
#             blog = Article.objects.create(title=title, author=author, content=content, date=date)
#             blog.save()
#             return redirect('blog:index')
#
#         else:
#             messages.info(request, 'Invalid Entry')
#             return redirect('blog:create_blog')
#
#     else:
#         form = BlogCreate()
#
#     return render(request, 'blog/blog_create.html', {'form': form})


@login_required(login_url="/login/")
def blog_edit(request, slug):
    blog = Article.objects.get(slug=slug)

    if request.method == 'POST':
        form = BlogCreate(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog:index')

        else:
            messages.info(request, 'Invalid Entry')
            return redirect('blog:create_blog')

    else:
        # prepopulated data with that slug instance
        form = BlogCreate(instance=blog)

    return render(request, 'blog/edit-blog.html', {'form': form})

@login_required(login_url="/login/")
def blog_delete(request, slug):
    blog = Article.objects.get(slug=slug)

    if request.method == 'POST':
        user = blog.user
        if request.user == user:
            blog.delete()
            return redirect('blog:index')
        else:
            return HttpResponse("<h1>Not a Valid user to delete this blog post</h1>")
    return render(request, 'blog/delete-blog.html', {'blog': blog})

