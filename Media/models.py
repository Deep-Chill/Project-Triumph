from django.db import models
from User.models import Profile
from Location.models import Country

class Newspaper(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name_of_newspaper = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    owners = models.ManyToManyField(Profile, related_name='newspapers')
    subscribers = models.IntegerField(default=0)
    def __str__(self):
        return self.name_of_newspaper
    '''create a method that adds a new subscriber to the newspaper'''
    def add_subscriber(self):
        self.subscribers += 1
        self.save()
    def remove_subscriber(self):
        self.subscribers -= 1
        self.save()

class Article(models.Model):
    title = models.CharField(null=False, max_length=100)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE, default='')
    content = models.TextField(null=False)
    date_published = models.DateField(auto_now_add=True, null=False)
    date_last_edited = models.DateField(auto_now=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    '''a method that adds a new subscriber to the newspaper'''
    def add_subscriber(self):
        self.subscribers += 1
        self.save()
    '''a method to create a new article'''
    def create_article(self, title, author, newspaper, content):
        self.title = title
        self.author = author
        self.newspaper = newspaper
        self.content = content
        self.save()

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default='')
    content = models.TextField(null=False)
    date_posted = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    def add_like(self):
        self.likes += 1
        self.save()
    def remove_like(self):
        self.likes -= 1
        self.save()
    def __str__(self):
        return self.content

###Create a signal to automatically add yourself as your friend

class SocialPosts(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default='')
    text = models.CharField(max_length=240)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.user.username} + {self.id} + {self.creation_date}"