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
    'en': ('en_US','%B %Y')
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
TEMPLATE_PAGES = {'pages/math-notes.html': 'notes/math-notes.html',
                  'pages/virt-machines.html': 'notes/virt-machines.html',
                  'pages/pythonemacs.html': 'notes/pythonemacs.html',
                  'pages/books.html':'notes/books.html'}

#=============
# Other
#=============
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
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
