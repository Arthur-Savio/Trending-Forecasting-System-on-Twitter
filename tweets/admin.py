from django.contrib import admin
from .models import SelectedTweet, Setup, TrendingTopics, Location

admin.site.register(SelectedTweet)
admin.site.register(Setup)
admin.site.register(TrendingTopics)
admin.site.register(Location)