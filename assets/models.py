from mongoengine import *
import datetime
import json
from django.db import models
from django.utils import timezone



class Show(Document):
    """ 
        represents the show of a specific channels
    """

    name=StringField(default='')
    chanel_id=StringField(default='')

    def __str__(self):
        return self.name

    def _get_show_data(self):
        return {'name':self.name}


class Episode(Document):
    """ 
        represents the episode of a specific show
    """
    name=StringField(default='')
    show_id=StringField(default='')
    episode_no=IntField(default=1)

    def __str__(self):
        return self.name

    def _get_episode_data(self):
        return {'name':self.name, 'episode_no':self.episode_no}


class Channel(Document):
    """ 
        represents channel presents in existing system
    """
    name=StringField(default='')

    def __str__(self):
        return self.name

    def _get_channel_data(self):
        return {'name':self.name}
