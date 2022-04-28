from django.contrib import admin
from appTwo.models import AccessRecord,Topic,Webpage,Users,UserProfilInfo

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Users)
admin.site.register(UserProfilInfo)
