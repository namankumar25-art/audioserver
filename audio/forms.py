from django.forms import ModelForm
from .models import Audiobook, Podcast, Song

class AudiobookForm(ModelForm):
	class Meta:
		model = Audiobook
		fields = '__all__'

class PodcastForm(ModelForm):
	class Meta:
		model = Podcast
		fields = '__all__'

class SongForm(ModelForm):
	class Meta:
		model = Song
		fields = '__all__'
