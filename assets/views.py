from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.generic import View as V
from api_utils.argument_parser import retrieve_request_arguments
from assets.models import Show, Episode, Channel


class MyChannel(V):
    def get(self, request):
        _id = retrieve_request_arguments(request, optional_query_parameters=['_id'])
        channel_qryset = Channel.objects.get(id=_id)
        return JsonResponse(channel_qryset._get_channel_data())

    def post(self, request):
        name = retrieve_request_arguments(request, compulsory_body_argument_names=['name'])
        Channel(name=name).save()
        return HttpResponse('result')


class MyShow(V):
    def get(self, request):
        _id = retrieve_request_arguments(request, optional_query_parameters=['_id'])
        show_qryset = Show.objects.get(id=_id)
        return JsonResponse(show_qryset._get_show_data())

    def post(self, request):
        name, channel_id = retrieve_request_arguments(request, compulsory_body_argument_names=['name', 'channel_id'])
        Show(name=name, channel_id=channel_id).save()
        return HttpResponse('result')


class MyEpisode(V):
    def get(self, request):
        _id = retrieve_request_arguments(request, optional_query_parameters=['_id'])
        episode_qryset = Episode.objects.get(id=_id)
        return JsonResponse(episode_qryset._get_episode_data())

    def post(self, request):
        name, show_id, episode_no = retrieve_request_arguments(request, compulsory_body_argument_names=['name', 'show_id', 'episode_no'])
        Episode(name=name, show_id=show_id, episode_no=episode_no).save()
        return HttpResponse('result')