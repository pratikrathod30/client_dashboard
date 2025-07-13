from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')
    description = models.TextField()
    designation = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name

class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
