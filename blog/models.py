from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

# User class

class Article(models.Model):
    article_image = models.ImageField(upload_to='images/', blank=True)
    article_title = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name='author', default=1, on_delete=models.CASCADE)
    article_about = models.TextField()
    slug = models.SlugField(unique=True, default=2)
    date_published = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.article_title


# snipping out first 50 characters of the Article about field, to be used in template to display out
    def snippet(self):
        return self.article_about[:51]


# gives out slug for a particular instance/object
    def get_absolute_url(self):
        return reverse('detail-blog', kwargs={'slug': self.slug})

# overiding save method for an instance that is created to generate slugs using article title
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.article_title)

        super(Article, self).save(*args, **kwargs)



