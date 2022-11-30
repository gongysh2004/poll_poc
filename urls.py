from django.contrib import admin
from django.urls import include, re_path
import polls
urlpatterns = [
    re_path(r'^polls/', include("polls.urls")),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls')),
]
