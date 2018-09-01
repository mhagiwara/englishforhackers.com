#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = '../pelican-themes/Flex'

AUTHOR = 'Masato Hagiwara'
SITEURL = 'http://localhost:8000'
SITENAME = u'エンジニア・研究者の英語学習'
SITETITLE = u'エンジニア・研究者の<br/>英語学習'
SITESUBTITLE = u'ソフトウェア・エンジニアや研究者のための英語学習情報。講演/トーク・技術記事・論文などの紹介'
SITEDESCRIPTION = SITESUBTITLE
SITELOGO = 'http://masatohagiwara.net/face.jpg'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = './Flex'
PATH = 'content'
TIMEZONE = 'America/New_York'

I18N_TEMPLATES_LANG = 'ja'
DEFAULT_LANG = 'ja'
OG_LOCALE = 'ja_JP'
LOCALE = 'ja_JP.UTF-8'

DATE_FORMATS = {
    'en': '%B %d, %Y',
    'ja': u'%Y-%m-%d(%a)',
}

DISABLE_URL_HASH = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

LINKS = (('個人ページ', 'http://masatohagiwara.net/'),
         ('Duolingo', 'http://www.duolingo.com/'),
         ('お問い合わせ', 'https://docs.google.com/forms/d/e/1FAIpQLSffbTFvdUXJhN4jTOmylcIRvlntKmaYVkIbYPrbBCPm0iC9Sw/viewform?usp=sf_link'))

SOCIAL = (('github', 'https://github.com/mhagiwara'),
          ('twitter', 'https://twitter.com/mhagiwara'),
          ('rss', 'feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-NonCommercial-ShareAlike',
    'version': '4.0',
    'slug': 'by-nc-sa'
}

COPYRIGHT_YEAR = 2017

DEFAULT_PAGINATION = 10

# PLUGIN_PATHS = ['./pelican-plugins']
# PLUGINS = ['sitemap', 'post_stats', 'i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

GOOGLE_ANALYTICS = 'UA-175204-11'

DISQUS_SITENAME = "englishforhackers"

# ADD_THIS_ID = 'ra-55adbb025d4f7e55'
#
# STATUSCAKE = {
#     'trackid': 'SL0UAgrsYP',
#     'days': 7,
#     'rumid': 6852,
#     'design': 6,
# }

STATIC_PATHS = ['images', 'extra']

EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/custom.css'},
}

CUSTOM_CSS = 'static/custom.css'

USE_LESS = True

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-7401771876348738',
    'page_level_ads': True,
    'ads': {
        'aside': '',
        'main_menu': '',
        'index_top': '',
        'index_bottom': '',
        'article_top': '',
        'article_bottom': '',
    }
}
