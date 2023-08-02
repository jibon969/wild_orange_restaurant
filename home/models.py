from django.db import models


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
    description = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=120)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Items(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    image = models.FileField(upload_to="items/")
    description = models.TextField()
    price = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

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
