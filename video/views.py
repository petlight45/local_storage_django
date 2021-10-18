from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import TemplateView


class PriceView(TemplateView):
    template_name = 'video/menu_price.html'


class VideoListView(TemplateView):
    template_name = 'video/menu_video_list.html'


class VideoView(TemplateView):
    template_name = 'video/view.html'
