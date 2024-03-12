# アプリケーションレベルのURL設定ファイル

from django.contrib import admin
from django.urls import path, include  # 'include'関数をインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    # 'alcohol'アプリのURL設定をインクルード
    path('my_alcohol_calculator/', include('my_alcohol_calculator.urls')),
]
