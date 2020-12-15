from django.urls import path, include
from . import views
from rest_framework import routers

#Routers allow us to create a get and a post request
router = routers.DefaultRouter()
router.register('courses', views.CourseView)   #The word courses will appear localhost/courses/
#Result will be a list with dictionaries inside them


#from this directory,import views
urlpatterns = [
    path('', include(router.urls)),
]
