from django.db import models
from datetime import datetime

# Create your models here.


class TutorialCategory(models.Model):
    tutorial_category = models.CharField(max_length=200)
    catetory_summary = models.CharField(max_length=200)
    catetory_slug = models.CharField(max_length=200)


# Gives the proper plural name for admin
# otherwise we got "Tutorial Category" in admin


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.tutorial_category


class TutorialSeries(models.Model):
    tutorial_series = models.CharField(max_length=200)
    series_summary = models.CharField(max_length=200)

    tutorial_category = models.ForeignKey(
        TutorialCategory, default=1, blank=True, verbose_name='Category', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Series'

    def __str__(self):
        return self.tutorial_series


class Tutorial(models.Model):
    tutorial_title = models.CharField(max_length=200)
    tutorial_content = models.TextField()
    tutorial_published = models.DateTimeField(
        'date published', default=datetime.now())
    tutorial_series = models.ForeignKey(
        TutorialSeries, default=1, verbose_name='Series', blank=True, on_delete=models.CASCADE)
    tutorial_slug = models.CharField(max_length=200, default=1)

    def __str__(self):
        return self.tutorial_title
