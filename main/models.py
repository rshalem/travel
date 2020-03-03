from django.db import models

# State model
class State(models.Model):
    state_title = models.CharField(max_length=100)
    state_image = models.ImageField(upload_to='images/', blank=True)
    state_about = models.TextField(default=1)

    class Meta:
        verbose_name = 'State'

    def __str__(self):
        return self.state_title


# City model, class represents the table in thd DB , added foreign key to the many side of the relationship
class City(models.Model):
    city_image = models.ImageField(upload_to='images/', blank=True)
    city_title = models.CharField(max_length=100)
    city_about = models.TextField()
    state = models.ForeignKey('State', related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return '{},{}'.format(self.city_title, self.city_about)

# Places to visit model, if related name not specified, django will create auto attribute named place_set

class Place(models.Model):
    place_image = models.ImageField(upload_to='images/', blank=True)
    place_title = models.CharField(max_length=100)
    place_about = models.TextField()
    city = models.ForeignKey('City', related_name='places', on_delete=models.CASCADE)

    def __str__(self):
        return '{},{}'.format(self.place_title, self.place_about)


