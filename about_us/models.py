from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)


class Cookies(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Faq(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Help(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class PolicyPolicy(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class TermsConditions(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Newsletter(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-timestamp']
