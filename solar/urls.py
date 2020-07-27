from django.urls import path
from solar.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='home_page_url'),
    path('<str:slug>/', Page_Controller.as_view(), name='page_url'),
    path(ststic_page_url('blog')+'/<str:slug>/', blog_detail,  name='blog_detail_url'),
    path(ststic_page_url('service')+ '/<str:slug>/', service_detail, name='service_detail_url'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
