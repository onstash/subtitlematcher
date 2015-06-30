#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

VIDEO_FORMAT = ('avi', 'flv', 'mkv', 'm4p', 'm4v',\
                'mp4', 'mpeg', 'mpg', 'webm', 'wmv')
SUBTITLE_FORMAT = ('ass', 'srt', 'ssa' ,'sub')

files_in_movie_dir = os.listdir(sys.argv[1] if len(sys.argv) > 1 else os.getcwd())

videos    = filter(lambda f: f.split('.')[-1] in VIDEO_FORMAT, files_in_movie_dir)
subtitles = filter(lambda f: f.split('.')[-1] in SUBTITLE_FORMAT, files_in_movie_dir)

print videos
print subtitles
