from django.conf.urls import url
from Injustice import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
        url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
]
    
