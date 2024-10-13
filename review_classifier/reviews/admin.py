from django.contrib import admin
from .models import Review

# Регистрируем модель Review в админке
admin.site.register(Review)
