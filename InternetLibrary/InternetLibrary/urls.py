from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers
from Application import views

router = routers.DefaultRouter()
router.register(r'v1/book', views.BookViewSet)
router.register(r'v1/author', views.AuthorViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/author/(?P<author>\d+)/book', views.BookDetailAPIView, name='detail')

]
