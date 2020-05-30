from . import views
from django.urls import path


urlpatterns = [
    path("<int:id>",  views.detail,name="detail"),
    path("rooms", views.rooms_list,name="rooms"),
    path("new",views.new,name="new"),

]
