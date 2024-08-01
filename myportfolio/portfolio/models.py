from django.db import models

class About(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About"

class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=True)  # Add URL field

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

class Contact(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    website = models.URLField(blank=True)  # Add website URL field
    linkedin = models.URLField(blank=True)  # Add LinkedIn URL field
    github = models.URLField(blank=True)  # Add GitHub URL field

    def __str__(self):
        return "Contact"

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.created_at}'

