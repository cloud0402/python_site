from django.db import models


# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(u'标题', max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField(u'创建时间')
    class Meta:
        ordering = ('-timestamp',)
