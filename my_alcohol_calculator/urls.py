# プロジェクトレベルのURL設定ファイル
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
