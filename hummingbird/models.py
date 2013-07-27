__author__ = 'Alex'


class Anime(object):

    def __init__(self, anime_dict, api):
        self.__dict__.update(anime_dict)
        self.api = api

    def update_library(self, params):
        self.api.update_library(self.slug, params=params)


class Entry(object):

    def __init__(self, entry_dict, api):
        self.__dict__.update(entry_dict)
        self.api = api


class Library(object):

    entries = []

    def __init__(self, library_list, api):
        self.api = api
        for entry_dict in library_list:
            self.entries.append(Entry(entry_dict, api))