from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer, PodcastSerializer, AudiobookSerializer
from audio.models import Song, Podcast, Audiobook


@api_view(['GET'])
def apioverview(request):

	api_urls={

		'audio_list':'api/<str:audio_type>/',
		'audio_detail':'api/<audio_type>/<audio_id>/',
		'audio_create':'api/<audio_type>/create/',
		'audio_update':'api/<audio_type>/<audio_id>/update/',
		'audio_delete':'api/<audio_type>/<audio_id>/delete/',
	}

	return Response(api_urls)

@api_view(['GET'])
def audio_list(request, audio_type):

	if audio_type=="song":

		songs=Song.objects.all()
		songs_serialized=SongSerializer(songs, many=True)

		return Response(songs_serialized.data)

	elif audio_type=="podcast":

		podcasts=Podcast.objects.all()
		podcasts_serialized=PodcastSerializer(podcasts, many=True)

		return Response(podcasts_serialized.data)

	elif audio_type=="audiobook":

		audiobooks=Audiobook.objects.all()
		audiobooks_serialized=AudiobookSerializer(audiobooks, many=True)

		return Response(audiobooks_serialized.data)

	else:
		return Response("No such Audiofile exists")

@api_view(['GET'])
def audio_detail(request, audio_type, audio_id):

	if audio_type=='song':
		song=Song.objects.get(id=audio_id)
		song_serialized=SongSerializer(song, many=False)

		return Response(song_serialized.data)

	elif audio_type=="podcast":

		podcast=Podcast.objects.get(id=audio_id)
		podcast_serialized=PodcastSerializer(podcast, many=False)

		return Response(podcast_serialized.data)

	elif audio_type=="audiobook":

		audiobook=Audiobook.objects.get(id=audio_id)
		audiobook_serialized=AudiobookSerializer(audiobook, many=False)

		return Response(audiobook_serialized.data)

	else:
		return Response("No such Audiofile exists")

@api_view(['POST'])
def audio_create(request, audio_type):

	if audio_type=='song':

		new_song_serialized=SongSerializer(data=request.data)

		if new_song_serialized.is_valid():
			new_song_serialized.save()

		return Response(new_song_serialized.data)

	elif audio_type=='podcast':

		new_podcast_serialized=PodcastSerializer(data=request.data)

		if new_podcast_serialized.is_valid():
			new_podcast_serialized.save()

		return Response(new_podcast_serialized.data)

	elif audio_type=='audiobook':

		new_audiobook_serialized=AudiobookSerializer(data=request.data)

		if new_audiobook_serialized.is_valid():
			new_audiobook_serialized.save()

		return Response(new_audiobook_serialized.data)

	else:
		return Response("Audiofile Cannot be Created")


@api_view(['POST'])
def audio_update(request, audio_type, audio_id):

	if audio_type=='song':

		song=Song.objects.get(id=audio_id)
		song_serialized=SongSerializer(instance=song, data=request.data)

		if song_serialized.is_valid():
			song_serialized.save()

		return Response(song_serialized.data)

	elif audio_type=='podcast':

		podcast=Podcast.objects.get(id=audio_id)
		podcast_serialized=PodcastSerializer(instance=podcast, data=request.data)

		if podcast_serialized.is_valid():
			podcast_serialized.save()

		return Response(podcast_serialized.data)

	elif audio_type=='audiobook':

		audiobook=Audiobook.objects.get(id=audio_id)
		audiobook_serialized=AudiobookSerializer(instance=audiobook, data=request.data)

		if audiobook_serialized.is_valid():
			audiobook_serialized.save()

		return Response(audiobook_serialized.data)

	else:
		return Response("Audiofile Cannot be Created")


@api_view(['DELETE'])
def audio_delete(request, audio_type, audio_id):
	if audio_type=='song':

		song=Song.objects.get(id=audio_id)
		song.delete()
		return Response("Song Deleted Successfully")

	elif audio_type=='podcast':

		podcast=Podcast.objects.get(id=audio_id)
		podcast.delete()
		return Response("Podcast deleted successfully")

	elif audio_type=='audiobook':

		audiobook=Audiobook.objects.get(id=audio_id)
		audiobook.delete()

		return Response("Audiobook deleted successfully")

	else:
		return Response("Audiofile Does not exist")