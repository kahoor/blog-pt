from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.
def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')

class Kind(models.Model):
    # TODO: make this thing choice drop
    short_scale = models.CharField( max_length=6)
    scale = models.CharField( max_length=30)
    
    def __str__(self):
        """Unicode representation of MeasurableThing."""
        return self.scale

def get_kind():
    return Kind.objects.get_or_create(short_scale='d', scale='This things kind was deleted. Please choose(or create) another kind ASAP')

class MeasurableThing(models.Model):
    """Model definition for MeasurableThing."""
    
    title = models.CharField(max_length=50)
    description = models.TextField(help_text='tell me about this measurable thing')
    user = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user))
    started = models.DateTimeField(auto_now=False, auto_now_add=True)
    kind = models.ForeignKey("Kind", on_delete=models.SET(get_kind))

    def __str__(self):
        """Unicode representation of MeasurableThing."""
        return self.title


class Records(models.Model):
    measurable_thing = models.ForeignKey("MeasurableThing", on_delete=models.CASCADE)
    ammount = models.IntegerField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        """Unicode representation of MeasurableThing."""
        return str(self.ammount)


