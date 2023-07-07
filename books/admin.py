from django.contrib import admin

# Register your models here.
from .models import Collection, Piece, Home

admin.site.register(Collection)
admin.site.register(Piece)
admin.site.register(Home)
