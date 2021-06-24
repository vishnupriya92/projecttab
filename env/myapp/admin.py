from django.contrib import admin
from myapp.models import Topic,Webpage,AccessDetails

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessDetails)