from django.urls import path
from . import views


urlpatterns = [
	path('', views.audioserverhome, name='audio-server'),
	path('<str:audio_type>/', views.audio_list, name = 'audio-list'),
	path('<str:audio_type>/<int:audio_id>/', views.audio_detail, name = 'audio-detail'),
	path('<str:audio_type>/create/', views.create, name = 'audio-create'),
	path('<str:audio_type>/<int:audio_id>/update/', views.update, name='audio-update'),
	path('<str:audio_type>/<int:audio_id>/delete/', views.delete, name='audio-delete'),
	
]