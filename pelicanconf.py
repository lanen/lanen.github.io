#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'evan'
SITENAME = u'浅析编程技术'
SITEURL = ''

PATH = 'content'

# 时区
TIMEZONE = 'Asia/Shanghai'

# 日期格式
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = u'zh'

# THEME = 'pelican-themes/bootstrap2'
THEME = 'my-themes/bootstrap2'

JINJA_EXTENSIONS = ['jinja2.ext.i18n']
#JINJA_ENVIRONMENT = ['jinja2.ext.i18n']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = ()
# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = 25

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
