from django.urls import path

from .views import (
    CCTVList,
    CCTVDetail,
)


urlpatterns = [
    path("", CCTVList.as_view(), name = CCTVList.name),
    path("<int:pk>/", CCTVDetail.as_view(), name = CCTVDetail.name),
]