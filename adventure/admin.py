from django.contrib import admin
# Register your models here.
from .models import Room, Player

class PlayerInline(admin.TabularInline):
    model = Player
    extra = 2

class RoomAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['title']}),
    ('Description', {'fields': ['description'], 'classes': ['collapse']}),]
    inline = [PlayerInline]

# admin.site.register(Room)
# admin.site.register(Player)
admin.site.register(Room, RoomAdmin)

