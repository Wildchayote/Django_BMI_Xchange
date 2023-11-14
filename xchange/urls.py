from django.urls import path
from xchange.views import mainform, conversion_result


urlpatterns = [
    path('process/', mainform, name = 'mainform'),
    path('output/<int:pk>/', conversion_result, name = 'conversion_result'),
]