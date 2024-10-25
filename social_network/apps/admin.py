from django.contrib import admin

from .models import Profile,Comment,Story,Post

admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Story)
admin.site.register(Post)
