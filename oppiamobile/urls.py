

from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    url(r'^', include('oppia.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^content/', include('content.urls')),
    url(r'^profile/', include('profile.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^activitylog/', include('activitylog.urls')),
    url(r'^viz/', include('viz.urls')),
    path(r'av', include('av.urls', namespace="oppia_av")),
    url(r'^gamification/', include('gamification.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^integrations/', include('integrations.urls')),
]
