from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.generic import View as V
from api_utils.argument_parser import retrieve_request_arguments
from assets.models import Show, Episode, Channel


class MyChannel(V):

    def get(self, request):

        _id = retrieve_request_arguments(request, optional_query_parameters=['_id'])
        print '_id is {}'.format(_id)
        channel_qryset = Channel.objects.get(id=_id)
        return JsonResponse(channel_qryset._get_channel_data())

    def post(self, request):

        name = retrieve_request_arguments(request, compulsory_body_argument_names=['name'])

        Channel(name=name).save()

        return HttpResponse('result')