from django.urls import path
from .views import SeriesListView,SeriesDetailView
urlpatterns = [
   path('', SeriesListView.as_view(), name='series_list'),
   path('<int:pk>', SeriesDetailView.as_view(),name='series_detail')
]