from django.urls import path
from .views import *

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('accounts/create/', create_user, name='create_user'),
    path('accounts/test/', authentication_test, name='authentication_test'),

    path('cars/', car_view, name='car_view'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)