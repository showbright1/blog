#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# =============
# Basic settings
# =============
AUTHOR = u'Michael Martinez'
SITENAME = u'MM'
DEFAULT_LANG = u'en'
SITEURL = 'http://michaelmartinez.in'
GITHUB_URL = 'http://github.com/MichaelMartinez'
TIMEZONE = 'America/Phoenix'
DATE_FORMATS = {
    'en': ('en_US', '%B %Y')
}
DEFAULT_DATE_FORMAT = ('%B %Y')

# =============
# Category/Feed settings
# =============
USE_FOLDER_AS_CATEGORY = (True)
DEFAULT_CATEGORY = ("notes")
PDF_GENERATOR = (False)
DELETE_OUTPUT_DIRECTORY = (True)
NEWEST_FIRST_ARCHIVES = (True)
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

# =============
# Template Pages settings
# Template pages are custom pages make a jinja2 template file
# Then make a path pointing from it to the destination like so
# =============
TEMPLATE_PAGES = {}

#=============
# Twitter Card
#=============
# https://dev.twitter.com/cards
TWITTER_CARD_USE = (True) #| False
#TWITTER_CARD_SITE = '@website' # The site's Twitter handle like @my_blog
#TWITTER_CARD_SITE_ID = 123456 # The site's Twitter ID
TWITTER_CARD_CREATOR = '@monkmartinez'  # Your twitter handle like @yourtwitname
#TWITTER_CARD_CREATOR_ID = 56789 # The site creator's id

#=============
# Other
#=============
LINKS = (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
         ('Python.org', 'http://python.org'),
         ('Jinja2', 'http://jinja.pocoo.org'),
         ('iPython', 'http://ipython.org/'),)
FILES_TO_COPY = [('CNAME', 'CNAME')]
STATIC_PATHS = ['images', 'ipynb']
#=============
# Theme Stuff
#=============
DEFAULT_PAGINATION = 5
THEME = "bootstrap-pelican"

#=============
# Plugins
#=============
PLUGIN_PATH = '/Users/michaelmartinez/Documents/code/python/twitter_card'
PLUGINS = ['twitter_card']
