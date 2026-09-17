from django.db import models


class Lead(models.Model):
    STATUS_CHOICES = [
        ("New", "New"),
        ("Contacted", "Contacted"),
        ("Qualified", "Qualified"),
        ('converted', 'Converted'),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Automation(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    trigger = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Active")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name