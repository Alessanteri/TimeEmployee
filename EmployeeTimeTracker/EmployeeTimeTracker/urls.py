from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('home.urls')),
    path('login/', include('loginmanager.urls')),
    path('message/', include('message.urls')),
    path('timecard/', include('timecard.urls')),
    path('test/', include('test.urls')),
)
# urlpatterns = [
#     path('i18n/', include('django.conf.urls.i18n')),
#     path('admin/', admin.site.urls),
#     path('', include('home.urls')),
#     path('login/', include('loginmanager.urls')),
#     path('message/', include('message.urls')),
#     path('timecard/', include('timecard.urls')),
#     path('test/', include('test.urls')),
# ]
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('home.urls')),
#     path('login/', include('loginmanager.urls')),
#     path('message/', include('message.urls')),
#     path('timecard/', include('timecard.urls')),
# ]
# urlpatterns += i18n_patterns(
#     path('test/', include('test.urls')),
# )
