from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from content.views import Main, UploadFeed
from .views import Sub
from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    # include 사용하면 앞에 설정 가능
    path('content/', include('content.urls')),
    path('user/', include('user.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
