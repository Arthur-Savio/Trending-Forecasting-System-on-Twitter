from django.urls import path
from tweets import views

urlpatterns = [
    path('selected_tweets/', views.SelectedTweetsListView.as_view()),
    path('locations/', views.LocationView.as_view()),
    path('setup/', views.SetupView.as_view()),
    path('trending/', views.TrendingTopicsView.as_view()),
    path('setup/<int:pk>/', views.SetupDetail.as_view()),
]

