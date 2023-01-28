from django.db import models

# Create your models here.
class Task(models.Model):
    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["-created"]

    title = models.CharField(max_length=350)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="static\images")

    def __str__(self):
        return self.title
