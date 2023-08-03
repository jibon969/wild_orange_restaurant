from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from embed_video.fields import EmbedVideoField


class AboutImage(models.Model):
    title = models.CharField(max_length=120)
    image1 = models.ImageField(upload_to="aboutImage/")
    image2 = models.ImageField(upload_to="aboutImage/")
    image3 = models.ImageField(upload_to="aboutImage/")
    image4 = models.ImageField(upload_to="aboutImage/")
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class About(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def category_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_pre_save_receiver, sender=Category)


class Item(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    image = models.FileField(upload_to="items/")
    description = models.TextField()
    price = models.PositiveIntegerField()
    slug = models.SlugField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def items_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(items_pre_save_receiver, sender=Item)


# Youtube Video link ( 3:02 Pm at 16/04/2020 )
class YoutubeVideo(models.Model):
    title = models.CharField(max_length=120)
    video = EmbedVideoField()  # same like models.URLField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title


class OnlineTableBook(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    subject = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OurClient(models.Model):
    name = models.CharField(max_length=200)
    message = models.TextField()
    profession = models.CharField(max_length=150, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
