from django.contrib import admin
from blog.models import Blogpost, Comment,Video

admin.site.register(Blogpost)
admin.site.register(Comment)
admin.site.register(Video)