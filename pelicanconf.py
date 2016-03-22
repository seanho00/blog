#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys
sys.path.append(os.curdir)
from cleanurls import *

AUTHOR = 'Sean Ho'
SITENAME = 'Sean\'s photoblog'
SITESUBTITLE = 'Now a family of three...'

FAVICON = '/images/seanho-icon.png'
HEADER_COVER = '/images/unsplash-Nte-4RiRfwU-fjord.jpg'

THEME = 'pelican-clean-blog'

TIMEZONE = 'America/Vancouver'
DEFAULT_LANG = 'en'
DEFAULT_DATE = 'fs'

PATH = 'content'
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_CATEGORY = "blog"
INDEX_SAVE_AS = 'index.html'
DIRECT_TEMPLATES = ['index', 'tags', 'categories']
DEFAULT_PAGINATION = 10
PAGINATED_DIRECT_TEMPLATES = ['index']

PLUGIN_PATHS = ['../plugins']
PLUGINS = ['assets', 'autopages', 'better_figures_and_images', 'gallery', 'gravatar', 'sitemap', 'photos']
SITEMAP = { 'format': 'xml' }

LINKS = (('Sean Ho', 'http://seanho.com/'),)
SOCIAL = (
    ('facebook', 'http://facebook.com/seanho00'),
    ('github', 'https://seanho00.github.com'),
    ('linkedin', 'http://www.linkedin.com/in/seanho00'),
)

# Cache generated pages
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
CACHE_PATH = '__pycache__'

# Settings for development server; overridden in publishconf.py
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
RELATIVE_URLS = True
