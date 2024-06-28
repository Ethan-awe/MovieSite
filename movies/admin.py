from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_year', 'genre', 'region')
    search_fields = ('title', 'genre', 'region')
    list_filter = ('region', 'release_year')

admin.site.register(Movie, MovieAdmin)
