from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils import timezone


User = get_user_model()
# Create your models here.


class Product(models.Model):

    TECHNOLOGY = 'IT'
    BUSINESS = 'BIZ'
    SPORTS = 'SP'
    ENTERTAINMENT = 'EN'
    POLITICS = 'POL'

    DOMAIN_CHOICES = (
        (TECHNOLOGY, 'Technology'),
        (BUSINESS, 'Business'),
        (SPORTS, 'Sports'),
        (ENTERTAINMENT, 'Entertainment'),
        (POLITICS, 'Politics'),
    )

    title = models.CharField(max_length=255)
    body = models.TextField()
    domain = models.CharField(max_length=3, choices=DOMAIN_CHOICES, default=POLITICS)
    slug = models.SlugField(allow_unicode=True, unique=True)
    image = models.ImageField(upload_to='image/')
    created_at = models.DateTimeField(default=timezone.now)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_products")

    class Meta:
        ordering = ['-created_at']

    def short_body(self):
        return self.body[:120]

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class UpVote(models.Model):
    product = models.ForeignKey(Product, related_name='vote', on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    