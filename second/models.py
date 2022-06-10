from django.db import models

from first.models import Movie

class Comment(models.Model):
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text[:20]



