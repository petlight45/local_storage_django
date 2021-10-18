from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
  raw_id_fields = ("user",)
  list_select_related = ("user",)
  list_display = ('user', 'name', 'video_url',)