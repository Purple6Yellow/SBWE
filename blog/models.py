
from django.conf import settings
from django.db import models
from django.utils import timezone

# opmerkingen in python module
# models.Model doet de code afwijken van eenvoudig python-klasse. Dit is echter noodzakelijk 
# aangezien django hierdoor weet dat het om een Django-model gaat

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish (self):
        self.published_date= timezone.now()
        self.save()

    def __str__(self):
        return self.title
