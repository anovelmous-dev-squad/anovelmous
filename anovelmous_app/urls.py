from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'novels', views.NovelViewSet)
router.register(r'chapters', views.ChapterViewSet)
router.register(r'tokens', views.TokenViewSet)
router.register(r'formatted_novel_tokens', views.FormattedNovelTokenViewSet)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls))
]