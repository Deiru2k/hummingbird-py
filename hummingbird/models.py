__author__ = 'Alex'


class Anime(object):
    
    """
    Contains info about anime accesible as object parameters.
    Also has an update_library method simmilar to one in Api.
    """
    
    
    def __init__(self, anime_dict, api):
        self.__dict__.update(anime_dict)
        self.api = api

    def update_library(self, **params):
        
        """
        Does the same as Api.update_library.
        Only this time you don't have to specify anime id.
        The only requirement is that user has to be authed.
        """
        
        self.api.update_library(self.slug, **params)


class Entry(object):

    """
    Contains info about user's libary entry, such as:
    * Rating
    * Episodes Watched
    * Times Rewatched
    and others.
    Also contains an anime object at Entry.anime.
    """
    
    def __init__(self, entry_dict, api):
        anime_dict = entry_dict.pop('anime')
        self.__dict__.update(entry_dict)
        self.api = api
        self.anime = Anime(anime_dict, api)
        
def Library(entries_list, api):
    entries = []
    for entry_dict in entries_list:
        entries.append(Entry(entry_dict, api))