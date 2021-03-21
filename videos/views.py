from django.shortcuts import render
from .models import Video   
from django.views.generic import ListView, DetailView
class VideoListView(ListView):
    model = Video
    template_name = 'videos.html'

class VideoDetailView(DetailView):
    model = Video
    template_name = 'video_detail.html'
