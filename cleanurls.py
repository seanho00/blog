#!/usr/bin/env python
# -*- coding: utf-8 -*- #
# Cleaner URLs in output dir: e.g., pages/about.md -> http://myblog.com/about
# In pelicanconf.py, do: "from cleanurls import *"

ARTICLE_URL             = '{category}/{slug}/'
ARTICLE_SAVE_AS         = '{category}/{slug}/index.html'
ARTICLE_LANG_URL        = '{category}/{slug}/{lang}.html'
ARTICLE_LANG_SAVE_AS    = '{category}/{slug}/{lang}.html'
DRAFT_URL               = 'draft/{slug}/'
DRAFT_SAVE_AS           = 'draft/{slug}/index.html'
DRAFT_LANG_URL          = 'draft/{slug}/{lang}.html'
DRAFT_LANG_SAVE_AS      = 'draft/{slug}/{lang}.html'
PAGE_URL                = '{slug}/'
PAGE_SAVE_AS            = '{slug}/index.html'
PAGE_LANG_URL           = '{slug}/{lang}.html'
PAGE_LANG_SAVE_AS       = '{slug}/{lang}.html'
CATEGORY_URL            = '{slug}/'
CATEGORY_SAVE_AS        = '{slug}/index.html'
TAG_URL                 = 'tag/{slug}/'
TAG_SAVE_AS             = 'tag/{slug}/index.html'
AUTHOR_URL              = 'author/{slug}/'
AUTHOR_SAVE_AS          = 'author/{slug}/index.html'

ARCHIVES_SAVE_AS        = ''
YEAR_ARCHIVE_SAVE_AS    = ''
MONTH_ARCHIVE_SAVE_AS   = ''
DAY_ARCHIVE_SAVE_AS     = ''
AUTHORS_SAVE_AS         = 'author/index.html'
CATEGORIES_SAVE_AS      = 'categories.html'
TAGS_SAVE_AS            = 'tag/index.html'
INDEX_SAVE_AS           = 'articles.html'

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)
