from django.db import models

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True)
    body = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}-{}".format(self.id, self.title)