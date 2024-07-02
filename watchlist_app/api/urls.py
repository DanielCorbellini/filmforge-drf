from django.urls import path
from watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlataformAV, StreamPlataformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-detail'),
    path('streamplataform/', StreamPlataformAV.as_view(), name='stream-plataform'),
    path('streamplataform/<int:pk>',
         StreamPlataformDetailAV.as_view(), name='stream-plataform-detail'),
]
