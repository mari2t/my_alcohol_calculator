from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alcohol_calculator/', include('alcohol_calculator.urls')),
]
