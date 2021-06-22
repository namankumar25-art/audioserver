from django.contrib import admin
from django.urls import path, include
from . import views

app_name="api"

urlpatterns=[

		path('', views.apioverview, name='api-overview'),
		path('<str:audio_type>/', views.audio_list,name='audio-list'),
		path('<str:audio_type>/<int:audio_id>/', views.audio_detail, name='audio-detail'),
		path('<str:audio_type>/create/', views.audio_create, name='audio-create'),
		path('<str:audio_type>/<int:audio_id>/update', views.audio_update, name='audio-update'),
		path('<str:audio_type>/<int:audio_id>/delete/', views.audio_delete, name='audio-delete'),

]