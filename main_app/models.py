from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500,blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']




