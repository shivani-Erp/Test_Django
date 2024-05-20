from django.contrib import admin
from .models import *

admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(QueryBuilderData)
admin.site.register(UploadedFile)
