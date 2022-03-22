from django.contrib import admin
from .models import Profile
from .models import user_profile

admin.site.register(Profile)
admin.site.register(user_profile)

