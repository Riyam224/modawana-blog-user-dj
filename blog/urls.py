from django.urls import path
from . import views 



urlpatterns = [
   path('' , views.home , name='home'),
   path("<int:pk>/", views.post_detail , name="post_detail"),
   path('about/' , views.about , name='about'),
   
]
