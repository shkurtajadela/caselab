from django.contrib import admin
from django.urls import path
from reviews.views import submit_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit_review/', submit_review, name='submit_review'),
]
