from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='books'
    )

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):

    class LanguageTypes(models.TextChoices):
        UZBEK   = 'uzbek'
        ENGLISH = 'english'
        RUSSIAN = 'russian'

    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    sale_percent = models.PositiveSmallIntegerField(default=0)
    best_seller = models.BooleanField(default=False)
    price = models.FloatField(default=0)
    pub_year = models.PositiveIntegerField(null=True)
    page_size = models.PositiveIntegerField(null=True)
    lang = models.CharField(max_length=50, choices=LanguageTypes.choices)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    file = models.FileField()
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):

        self.slug = slugify(self.title)

        return super().save(*args, **kwargs)






