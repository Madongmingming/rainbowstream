from .colors import *

# 'search': max search record
SEARCH_MAX_RECORD = 5
# 'home': default number of home's tweets
HOME_TWEET_NUM = 5
# 'allrt': default number of retweets
RETWEETS_SHOW_NUM = 5
# 'inbox','sent': default number of direct message
MESSAGES_DISPLAY = 5
# 'trend': max trending topics
TREND_MAX = 10
# 'switch': Filter and Ignore list ex: ['@fat','@mdo']
ONLY_LIST = []
IGNORE_LIST = []

# Autocomplete history file name
HISTORY_FILENAME = 'completer.hist'

USER_DOMAIN = 'userstream.twitter.com'
PUBLIC_DOMAIN = 'stream.twitter.com'
SITE_DOMAIN = 'sitestream.twitter.com'
DOMAIN = USER_DOMAIN

IMAGE_SHIFT = 10
IMAGE_MAX_HEIGHT = 40

# Following 16 basic colors is supported:
#   default
#   black
#   red
#   green
#   yellow
#   blue
#   magenta
#   cyan
#   grey
#   light_red
#   light_green
#   light_yellow
#   light_blue
#   light_magenta
#   light_cyan
#   white

TWEET = {
    'nick'      : grey,
    'clock'     : grey,
    'id'        : grey,
    'favourite' : light_green,
    'rt'        : grey,
    'link'      : light_cyan,
    'keyword'   : on_light_yellow,
}

MESSAGE = {
    'sender'    : grey,
    'recipient' : grey,
    'to'        : light_magenta,
    'clock'     : grey,
    'id'        : grey,
}

PROFILE = {
    'statuses_count'    : light_green,
    'friends_count'     : light_green,
    'followers_count'   : light_green,
    'nick'              : grey,
    'profile_image_url' : light_cyan,
    'description'       : light_yellow,
    'location'          : light_magenta,
    'url'               : light_cyan,
    'clock'             : white,
}

TREND = {
    'url': light_cyan
}