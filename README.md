Hummingbird API Wrapper, v0.1
=============================

A wrapper for Hummingbird.me API.
Hummingbird is a new way to Keep track of your anime, Discover new anime and share your thoughts with the community!

*Notice*: In it's current state, API is incomplete. 
This wrapper covers all functionality provided right now, and will be updated as more features are implemented.
Stay tuned.

Using API:
----------

To begin making use of API and this wrapper, you'll have to sign up for [Mashape](http://mashape.com)
Once you're there, create a production key and allow it to use [Hummingbird API](https://www.mashape.com/vikhyat/hummingbird-v1)
You can also use your testing key, but make sure that you ARE NOT using it in production.

Now, to start the actualy querying, you have to instanciate api using your mashape key, like that:

```python
from hummingbird.api import Api
api = Api('your_mashape_key')

anime = api.get_anime('steins-gate')
print anime
```

Use pydoc or help() to get the list of available methods.
_real docs coming soon_
