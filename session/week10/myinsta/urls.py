from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from posts.views import *
from rest_framework import routers, permissions
from accounts_token.views import login_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register('posts', PostModelViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Snippets API',
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/polices/terms/",
        contact=openapi.Contact(email="contact@scippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Function Based View
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    # Class Based View
    path('cbv/', class_view.as_view()),  # as_view: 진입 메소드

    # path('', index, name='index'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateView.as_view(), name='post-detail'),
    # path('posts/', include('posts.urls', namespace='posts')),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    path('', include(router.urls)),
    path('login/', login_view),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0),
         name='schema-json'),
    path('swagger/', schema_view.with_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
# 이미지 파일들이 설정된 폴더에 생성
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
