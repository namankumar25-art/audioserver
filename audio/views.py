from django.shortcuts import render, redirect, get_object_or_404
from .models import Audiobook, Podcast, Song
from django.http import HttpResponse
from .forms import AudiobookForm, PodcastForm, SongForm

def home(request):

	context={

		'audiobook':Audiobook.objects.all(),
		'podcast': Podcast.objects.all(),
		'song':Song.objects.all()
	}
				
	return render(request, 'audio/home.html', context)

def about(request):

	return render(request, 'audio/about.html', {'title': 'About'})

def audioserverhome(request):
	return render(request, 'audio/audioserverhome.html')

def audio_list(request, audio_type):	
	
	if audio_type == "audiobook":
		context = {'audio_type':'audiobook','audiobook': Audiobook.objects.all()}
		# return render(request, "audio/audio_list.html", context)

	elif audio_type == "podcast":
		context = {'audio_type':'podcast','podcast': Podcast.objects.all()}
		# return render(request, "audio/audio_list.html", context)

	elif audio_type == "song":
		context = {'audio_type':'song','song': Song.objects.all()}

	return render(request, "audio/audio_list.html", context)

def audio_detail(request, audio_type, audio_id):
	
	if audio_type == "audiobook":
		context = {'audio_type':'audiobook','audiobook': Audiobook.objects.get(id = audio_id)}
		# return render(request, "audio/audio_detail.html", context)

	elif audio_type == "podcast":
		context = {'audio_type':'podcast','podcast': Podcast.objects.get(id = audio_id)}
		# return render(request, "audio/audio_detail.html", context)

	elif audio_type == "song":
		context = {'audio_type':'song','song': Song.objects.get(id = audio_id)}
	
	return render(request, "audio/audio_detail.html", context)


def create(request, audio_type):
	
	if audio_type == "audiobook":

		if request.method=="POST":
			form=AudiobookForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect("audio-list", audio_type='audiobook')
		else:
			form = AudiobookForm()

	elif audio_type == "podcast":

		if request.method=="POST":
			form=PodcastForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect("audio-list", audio_type='podcast')
		else:
			form = PodcastForm()

	elif audio_type == "song":

		if request.method=="POST":
			form=SongForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect("audio-list", audio_type='song')
		else:
			form = SongForm()

	return render(request, "audio/create.html", {'form':form})


def update(request, audio_type, audio_id):

	if audio_type == 'audiobook':
		audio = Audiobook.objects.get(id=audio_id)
		# form = AudiobookForm(instance=audio)

		if request.method == 'POST':
			form = AudiobookForm(request.POST, instance=audio)
			if form.is_valid():
				form.save()
				return redirect('audio-detail', audio_type='audiobook', audio_id=audio_id)
		else:
			form = AudiobookForm()

	elif audio_type == 'podcast':
		audio = Podcast.objects.get(id=audio_id)
		# form = PodcastForm(instance = audio)

		if request.method == 'POST':
			form = PodcastForm(request.POST,instance = audio)
			if form.is_valid():
				form.save()
				return redirect('audio-detail', audio_type='podcast', audio_id=audio_id)

		else:
			form = PodcastForm()

	elif audio_type == 'song':
		audio = Song.objects.get(id=audio_id)
		# form = SongForm(instance= audio)

		if request.method =='POST':
			form = SongForm(request.POST,instance= audio)
			if form.is_valid():
				form.save()
				return redirect('audio-detail', audio_type='song', audio_id=audio_id)

		else:
			form = SongForm()

	return render(request, "audio/create.html", {'form':form})

def delete(request, audio_type, audio_id):

	if audio_type=="audiobook":
		audio=Audiobook.objects.get(id=audio_id)

		if request.method=='POST':
			audio.delete()
			context = {'audio_type':audio_type,'audio_id':audio_id}
			return redirect('audio-list', audio_type='audiobook')
		else:
			context = {'audio_type':audio_type,'audio_id':audio_id}

	elif audio_type == 'podcast':
		audio=Podcast.objects.get(id=audio_id)
		if request.method=='POST':
			audio.delete()
			context = {'audio_type':audio_type,'audio_id':audio_id}
			return redirect('audio-list', audio_type='podcast')
			
		else:
			context = {'audio_type':audio_type,'audio_id':audio_id}

	elif audio_type =='song':
		audio=Song.objects.get(id=audio_id)

		if request.method=='POST':
			audio.delete()
			context = {'audio_type':audio_type,'audio_id':audio_id}
			return redirect('audio-list', audio_type='song')
			
		else:
			context = {'audio_type':audio_type,'audio_id':audio_id}				
	
	return render(request, "audio/delete.html", context)