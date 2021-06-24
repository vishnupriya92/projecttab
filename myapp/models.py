from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name=models.CharField(max_length=30,unique=True,help_text="Topic name should be specified")

    def __str__(self):
        return self.top_name
    
class Webpage(models.Model):
    topic=models.ForeignKey(Topic, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField(max_length=100)
    desc=models.TextField(max_length=100)


    def __str__(self):
        return self.name

class AccessDetails(models.Model):
    Webpage=models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date_time=models.DateTimeField(auto_now=False,auto_now_add=False)

    def __str__(self):
        return self.Webpage.name
