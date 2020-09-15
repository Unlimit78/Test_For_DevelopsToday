from django.urls import path

from .views import PostViewSet, CommentViewSet

urlpatterns = [
    path(
        "api/post/",
        PostViewSet.as_view({"get": "list", "post": "create"}),
        name="post-list",
    ),
    path(
        "api/post/<int:pk>/",
        PostViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="post-detail",
    ),
    path(
        "api/comment/",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="comment-list",
    ),
    path(
        "api/comment/<int:pk>/",
        PostViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="comment-detail",
    ),
]
