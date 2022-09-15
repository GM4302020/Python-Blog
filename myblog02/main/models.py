from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class BlogTag(models.Model):
    name = models.CharField('Name', max_length=60, blank=False, null=False)
    slug = models.SlugField('Slug', editable=False, max_length=180, unique=True, default=timezone.now)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = str(self.name).strip().replace(' ', '-')
        super().save(*args, **kwargs)


# Create your models here.

class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,
                            verbose_name='Author')
    title = models.CharField('Title', max_length=120, blank=False, null=False)
    slug = models.SlugField('Slug', editable=False, max_length=180, unique=True, default=timezone.now)
    content = models.TextField('Content', max_length=800, blank=False, null=False)
    banner = models.ImageField('Image', upload_to='images/', blank=True,
                                 null=True, default='images/default_image.png')
    tags = models.ManyToManyField(BlogTag, verbose_name='Tags')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = str(self.title).strip().replace(' ', '-')
        super().save(*args, **kwargs)

'''

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,
                            verbose_name='User')
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, blank=False, null=False,
                            verbose_name='Post')
    review = models.TextField('Review', max_length=200, blank=False, null=False)

    def __str__(self):
        if len(self.review) >= 10:
            return self.review[:10] + ' ...'
        else:
            return self.review

    '''