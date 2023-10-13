from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('jardin/', views.jardin_view, name="jardin"),
    path('fermiers/', views.fermiers_view, name="fermiers"),
    path('create_edit_fermier/<int:id>/', views.create_edit_fermier_view, name="create_edit_fermier"),
]
