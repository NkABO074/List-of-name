from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('submit/',views.submit_form,name='submit_form'),
    path('inscription/',views.inscriptionView,name='inscription'),
    path('delete_dude/<int:dude_id>/',views.delete_dude,name='delete_dude'),
    path('update/<int:dude_id>/',views.update_dude,name='update'),
    path('search/',views.search_dude,name='search')
]