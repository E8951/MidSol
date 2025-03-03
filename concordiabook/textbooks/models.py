from django.db import models

# Create your models here.
class Textbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, blank=True, null=True)
    condition_choices = [
        ('new', 'Like New'),
        ('written', 'Written In'),
        ('old', 'Old'),
    ]
    condition = models.CharField(max_length=20, choices=condition_choices)
    course_code = models.CharField(max_length=20)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"