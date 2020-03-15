from blog.models import Article
from blog.forms import BlogCreate
from django.contrib import messages
from django.shortcuts import render, redirect




# blog homepage



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

def create_blog(request):
    if request.method == 'POST':
        form = BlogCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')

        else:
            messages.info(request, 'Invalid Entry')
            return redirect('blog:create_blog')

    else:
        form = BlogCreate()

    return render(request, 'blog/blog_create.html', {'form': form})


def index(request):
    all_article = Article.objects.all().order_by('-date_published')
    return render(request, 'blog/index.html', {'all_article': all_article})



def blog_detail(request, slug):
    single_blog = Article.objects.get(slug=slug)
    return render(request, 'blog/blog_detail.html', {'single_blog': single_blog})


