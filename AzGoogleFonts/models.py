from django.db import models
from django.urls import reverse


class FontGroups(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'font group'
        verbose_name_plural = 'font groups'

    def __str__(self):
        return self.name


class FontDesigners(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'font designer'
        verbose_name_plural = 'font designers'

    def __str__(self):
        return self.name


class AzGoogleFonts(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    font_group = models.ForeignKey(FontGroups, on_delete=models.CASCADE)
    designer = models.ForeignKey(FontDesigners, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-added',)
        verbose_name = 'font name'
        verbose_name_plural = 'font names'

    def get_designer_url(self):
        return reverse('designer', args=[self.designer.slug])

    def get_group_url(self):
        return reverse('group', args=[self.font_group.slug])

    def __str__(self):
        return self.name
