from django.urls import path
from .views import HomePageView,AccountPageView,SearchRepositoriesView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("account", AccountPageView.as_view(), name="account" ),
  path('search', SearchRepositoriesView.as_view(), name='search-repositories'),

]