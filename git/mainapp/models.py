from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25,null=False)
    usermail = models.EmailField(max_length=25,null=False)
    userpass = models.CharField(max_length=20,null=False)
    def __str__(self):
        return self.username
class Title(models.Model):
    title = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.title
class Content(models.Model):
    title = models.ForeignKey(Title,on_delete=models.CASCADE,null=True)
    filename = models.CharField(max_length=100,null=True)
    content_title = models.CharField(max_length=20,null=True)
    content = models.TextField(null=True)
    content_time = models.DateTimeField(auto_now_add=True,null=True)
    link_href = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.content
