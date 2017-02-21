from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=_('Author of the post'))
    title = models.CharField(max_length=50, verbose_name=_('Title'))
    content = models.TextField(verbose_name=_('Content'))
    dt_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation datetime'))
