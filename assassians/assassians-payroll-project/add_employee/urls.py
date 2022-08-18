from atexit import register
from django.contrib import admin
from django.urls import path, include
from add_employee import views

urlpatterns = [
    path('',views.dashboard ),
    path('show',views.dashboard ),

    path('reg_form/', views.form, name="form"),
    path('more', views.more ,name="more"),
    path('edit',views.edit,name="edit"),
    path('RecordEdited',views.RecordEdited),
    path('delete',views.delete),
]
