from django.db import models

# Create your models here.
class URLmap(models.Model):
    long_url=models.CharField(max_length=256)
    short_url=models.CharField(max_length=16)
    def __str__(self):
        return "Short URL for ->{} is {}".format(self.long_url,self.short_url)
class URLmanage(models.Model):
    lurl=models.CharField(max_length=256)
    surl=models.CharField(max_length=16)
    count=models.IntegerField(default=0)
    def __str__(self):
        return "Short URL for ->{} is {}".format(self.lurl,self.surl)

