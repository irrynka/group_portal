from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Role(models.Model):
    PERMISSION_CHOOSE = [
        ("User","Користувач"),
        ("Admin","Адмін"),
        ("Moderator","Модератор"),
    ]
    name = models.CharField(max_length=32 ,choices=PERMISSION_CHOOSE)


class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

###################################################################################

class Poll(models.Model):
    topic = models.CharField(max_length=128)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.topic}

class PollOption(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    text = models.TextField()

class Vote(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    poll_option = models.CharField(max_length=128)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Mate:
        unique_together = ("poll_id", "user_id")

    def __str__(self):
        return f"{self.poll_id} {self.user_id.first_name} - {self.user_id.last_name}"

###################################################################################   

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.user.last_name} {self.created_at}"



class PortfolioFile(models.Model):
    TYPE_CHOOSE = [
        ("File","Файл"),
        ("Link","Посилання"),
    ]
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    type = models.CharField(max_length=16, choices=TYPE_CHOOSE)
    url = models.URLField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to="portfolio_media/", blank=True, null=True)

    def clean(self):
        if self.type == "file" and not self.file:
            raise ValidationError("Файл обов'язковий для типу 'file'")
        if self.type == "url" and not self.url:
            raise ValidationError("Посилання обов'язковий для типу 'url'")


###################################################################################

class Galery(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_galleries')
    type = models.CharField(max_length=16)
    moderated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moderated_galleries')
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="galery_media/", blank=True, null=True)

    def __str__(self):
        return f"{self.creator.username} {self.created_at}"

###################################################################################

class Subject(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return {self.name}

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    value = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} {self.subject} {self.value}"




