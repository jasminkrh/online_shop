from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class Product(models.Model):

    class Meta:
        """ ordering = ['costs', 'type', 'location'] """
        verbose_name = 'Product'
        verbose_name_plural = 'Product'

    TYPE = [
        ('S', 'schokolade'),
        ('G', 'gummibaerchen'),
        ('K', 'kaugummis'), 
        ('B', 'bonbons')
    ]

    type = models.CharField(
        max_length=1,
        choices=TYPE
    )

    title = models.CharField(max_length=50)

    price= models.FloatField()

    description = models.CharField(max_length=200)


class Rating(models.Model):

    text = models.TextField(max_length=500)
    """ star rating """
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

    def get_comment_excerpt(self):
        if len(self.text) > 50:
            return self.text[:50] + '...'
        else:
            return self.text

    def __str__(self):
        return f'{self.get_comment_excerpt()} ({self.user.username})'

    def __repr__(self):
        return f'{self.get_comment_excerpt()} ({self.user.username} / {str(self.timestamp)})'

""" 
class Vote(models.Model):

    VOTE_TYPES = [
        ('1', '1'),
        ('2', '2'),
    ]

    up_or_down = models.CharField(max_length=1, choices=VOTE_TYPES)

    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    holiday_housing = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.up_or_down} on {self.holiday_housing} by {self.user.username}'

    def __repr__(self):
        return f'{self.up_or_down} on {self.holiday_housing} by {self.user.username} ({self.timestamp})'

 """