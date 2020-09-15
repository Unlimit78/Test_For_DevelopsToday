from celery import shared_task
from .models import Post


@shared_task
def reset_upvoutes():
    for post in Post.objects.all():
        post.amount_of_upvoutes = 0
        post.save()
