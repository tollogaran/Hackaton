from django.contrib import admin
from .models import Sala

# Register your models here.
class SalaAdmin(admin.ModelAdmin):
	pass

admin.site.register(Sala,)
