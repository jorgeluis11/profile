from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class ProjectManager(models.Manager):
    def top(self):
        return "Manager"


def get_url_large(self, filename):
    return 'media/img/large/%s' % (filename)


def get_url_medium(self, filename):
    return 'img/medium/%s' % (filename)


class Projects(models.Model):
    title = models.TextField(max_length=55)
    large = models.ImageField(upload_to=get_url_large)
    url = models.TextField(max_length=55)
    # medium = models.ImageField(upload_to=get_url_medium,blank=True)
    # medium = models.ImageField(upload_to=get_url_medium,blank=True)
    medium = ImageSpecField(source='large',
                            # processors=[ResizeToFill(400, 400)],
                            format='JPEG',
                            options={'quality': 60})
    description = models.TextField(max_length=2000)
    submit_date = models.DateTimeField(('date/time submitted'),
        default=timezone.now())
    visible = models.BooleanField(default=False)
    user_rating = models.IntegerField(default=0)
    visits = models.IntegerField(default=0)
    slug = AutoSlugField(populate_from='title', unique=True)
    objects = ProjectManager()
