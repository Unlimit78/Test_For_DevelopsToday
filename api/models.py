from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    amount_of_upvoutes = models.IntegerField()
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author_name = models.CharField(max_length=50)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
