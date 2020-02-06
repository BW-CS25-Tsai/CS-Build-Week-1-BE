from django.contrib import admin
# Register your models here.
from .models import Room

admin.site.site_header = 'Adventure Admin'
admin.site.site_title = 'Adventure Admin Area'
admin.site.site_title = 'Welcome to the Pollster admin area'

# class PlayerInline(admin.TabularInline):
#     model = Player
#     extra = 2

# class RoomAdmin(admin.ModelAdmin):
#     fieldsets = [(None, {'fields': ['title']}),
#     ('Description', {'fields': ['description'], 'classes': ['collapse']}),]
#     inline = [PlayerInline]

admin.site.register(Room)
# admin.site.register(Player)
# admin.site.register(Room, RoomAdmin)

