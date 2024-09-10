from django.shortcuts import render, redirect

# Create your views here.
import os
from django.conf import settings
from .models import Video
from .forms import VideoUploadForm
import subprocess
from .text_ccextractor import test_ccextractor

def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()

            # Process the video to extract subtitles
            video_file_path = os.path.join(settings.MEDIA_ROOT, video.video_file.name)
            subtitle_file_path = os.path.join(settings.SUBTITLE_UPLOAD_PATH, f'{video.pk}.srt')

            # Ensure the subtitle directory exists
            os.makedirs(os.path.dirname(subtitle_file_path), exist_ok=True)

            # Generate subtitles and save in subtitle folder
            test_ccextractor(video_file_path, subtitle_file_path)

            # Save the subtitle file to the model
            video.subtitle_file = f'subtitles/{video.pk}.srt'
            video.save()

            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'upload.html', {'form': form})


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'list.html', {'videos': videos})
