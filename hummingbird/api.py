import urllib
import urllib2
import json

from hummingbird.models import *

class AuthException(Exception):
    
    """
    Exception is thorwn if your mashape key is invalid. 
    Or your key is not allowed to query hummingbird. Who cares
    Classes with only __init__ is bad, let alone exceptions, yeah, I know.
    DEAL WITH IT
    """
    
    def __init__(self, key):
        Exception.__init__(self, "Invalid Mashape Key. Please check if your key is valid or if it is allowed to query\
         Hummingbird API.")
        self.api_key = key


class Api(object):
    
    """
    So yeah, this is like... Api?
    __init__ takes your mashape key as it's only agrument
    """
    
    headers = {}
    api_url = 'https://hummingbirdv1.p.mashape.com'
    
    def __init__(self, mashape_key):
        
        """
        :mashape_key: - Your mashape key. 
        Make sure that your key is allowed to query hummingbird
        If your key is invalid, raises AuthException
        """
        
        self.headers['X-Mashape-Authorization'] = mashape_key
        self.__test_key()
    
    def __test_key(self):
        
        """
        Used to test your key against mashape api
        """
        
        req = urllib2.Request(self.api_url+'/anime/', headers=self.headers)
        try:
            urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            if e.code == 404:
                return True
            elif e.code == 403:
                print e.read()
                raise AuthException(self.headers['X-Mashape-Authorization'])
    
    def __query(self, path, method, params=None):
        
        if not params:
            params = {}
        
        """
        Internal method used to simplify requests.
        """
        
        data = urllib.urlencode(params)
        if method == "POST":
            request = urllib2.Request(self.api_url+path, data=data, headers=self.headers)
            response = urllib2.urlopen(request)
            return response.read()
        elif method == 'GET':
            if data:
                url = self.api_url + '%s?%s' % (path, data)
            else:
                url = self.api_url + path
            print url
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            return json.loads(response.read())
    
    def authenticate(self, email, password):
        
        """
        Use this to authenticate your user.
        Arguments are self-explanatory.
        Returns user auth token that you can store for use later.
        """
        
        path = '/users/authenticate'
        params = {'email': email, 'password': password}
        self.user_key = self.__query(path, 'POST', params).strip('"')
        return self.user_key
    
    def get_anime(self, anime_id):
        
        """
        Gets anime info using anime id.
        Vik has not yet implemented search, so if you're going to use API
        in it's current state (god why) you'll have to think of some way
        to get the ID.
        """
        
        path = '/anime/' + anime_id
        return Anime(self.__query(path, 'GET'), self)
    
    def get_library(self, user_id='me', status='currently-watching', page=None):
        
        """
        Fetches library info for given user.
        status parameter represents the section of library you want to fetch.
        Status can be: currently-watching, on-hold, dropped, completed, plan-to-watch
        And yeah, there's no way to search for users either, so you'll have to
        think of some way to get user_id.
        """
        
        params = dict()
        params['status'] = status
        if user_id == 'me':
            params['auth_token'] = self.user_key
        if page:
            params['page'] = page
        path = '/users/' + user_id + "/library/"
        return Library(self.__query(path, 'GET', params), self)
    
    def update_library(self, anime_id, **params):
        
        """
        Updates user's library.
        Api.authenticate.
        Possible params are:
            privacy - [private\public] Wut?
            rating - [Number from 1 to 5] Anime rating. Stated as "Coming soon" but confirmed for working allready.
            rewatched_times - [number] Number of times user re-watched anime.
            notes - [string] User's personal notes about this anime
            episodes_watched - [number] Number of episodes watched
            increment_episodes - [bool] Wheter or not to increment episodes count with this update
        """

        params['auth_token'] = self.user_key
        path = '/libraries/' + anime_id
        
        return self.__query(path, 'POST', params)