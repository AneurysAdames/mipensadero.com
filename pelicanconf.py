#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "David Barragán"
SITENAME = "Mi Pensadero"
SITEURL = "http://mipensadero.com"

TIMEZONE = "Europe/Madrid"
DEFAULT_LANG = "es"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Static content
STATIC_PATHS = [
    "images",
    "media",
    'extra/robots.txt',
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

# Blogroll
LINKS =  (
    ("Kaleidos", "http://kaleidos.net"),
    ("PIWeek", "http://piweek.es/"),
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/bameda"),
    ("github", "https://github.com/bameda"),
    ("linkedin", "https://www.linkedin.com/in/davidbarraganmerino"),
)

# Plugins
PLUGIN_PATH = "plugins"
PLUGINS = ["gzip_cache", "sitemap",]

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Theme configuration
THEME = "/home/mipensadero/mipensadero.com/theme/"
DOCUTIL_CSS = True
TAG_CLOUD_MAX_ITEMS = 10

GITHUB_USER = "bameda"
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

GITHUB_USER_2 = "kaleidos"
GITHUB_SKIP_FORK_2 = True
GITHUB_SHOW_USER_LINK_2 = True
