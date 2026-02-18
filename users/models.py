from django.db import models
from django.contrib.auth.models import User


class Role(models.Model):
    name = models.CharField(max_length=32)


class UserRole(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)



class Poll(models.Model):
    topic = models.CharField(max_length=128)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.topic}"

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

    


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} - {self.user.last_name} {self.created_at}"



class PortfolioFile(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    file = models.FileField(null=True)
    url = models.CharField(max_length=100, null=True)

class Galery(models.Model):
    type = models.CharField(max_length=10)
    file = models.FileField(null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_galleries')
    type = models.CharField(max_length=16)
    moderated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moderated_galleries')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.creator.username} {self.created_at}"

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




