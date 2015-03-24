from django.conf.urls import url, include
from django.contrib import admin
import rest_framework
from rest_framework_nested import routers
from api import views


class DefaultRouter(rest_framework.routers.DefaultRouter, routers.SimpleRouter):
    pass


router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'novels', views.NovelViewSet)
router.register(r'chapters', views.ChapterViewSet)
router.register(r'tokens', views.TokenViewSet)
router.register(r'novel_tokens', views.NovelTokenViewSet)
router.register(r'formatted_novel_tokens', views.FormattedNovelTokenViewSet)
router.register(r'votes', views.VoteViewSet)

novel_router = routers.NestedSimpleRouter(router, r'novels', lookup='novel')
novel_router.register(r'chapters', views.ChapterViewSet)

urlpatterns = [
    url(r'^$', views.index),
    url(r'^api/', include(router.urls)),
    url(r'^api/', include(novel_router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls))
]