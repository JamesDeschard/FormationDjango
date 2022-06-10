from django.urls import path

from first.views import *

urlpatterns = [
    path('', home, name='home'),
    path('file/', file_example, name='file_example'),
    path('stream/', stream_example, name='stream_example'),
    path('json/', json_example, name='json_example'),
    path('api/', display_film_api, name='api'),

    path('classview', MovieView.as_view(), name='classview'),


    path('apidetail/<int:year>/', display_film_detail_api, name='api_specific'),


    path('kwargs/<int:name>/<str:str>/', kwargs_example, name='kwargs_example'),

]   