from django.contrib import admin
from .models import Audiobook
from .models import Podcast
from .models import Song

admin.site.register(Audiobook)
admin.site.register(Podcast)
admin.site.register(Song)
