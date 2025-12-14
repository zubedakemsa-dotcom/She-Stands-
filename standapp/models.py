from django.db import models

# Resources for women and girls
class Resource(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# Mentorship programs
class Mentor(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

# Survivor or inspirational stories
class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

# Contact messages from users
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
