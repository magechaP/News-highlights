import urllib.request,json
from .models import Source
from .models import Article

# Getting api key
api_key = None
# Getting the Category url
sources_url = None
#Getting the Article url
everything_url = None
#Search url
search_url = None