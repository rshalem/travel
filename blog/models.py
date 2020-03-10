from django.db import models
from django.urls import reverse



class Author(models.Model):
    author_name = models.CharField(max_length=50)
    author_about = models.TextField()

    def __str__(self):
        return self.author_name

    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'author_id': self.id})

class Article(models.Model):
    article_image = models.ImageField(upload_to='images/', blank=True)
    article_title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    article_about = models.TextField()
    slug = models.SlugField()
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.article_title


# snipping out first 50 characters of the Article about field, to be used in template to display out
    def snippet(self):
        return self.article_about[:50]


# gives out slug for a particular instance/object
    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})


