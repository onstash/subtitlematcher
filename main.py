#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

movie_dir = sys.argv[1] if len(sys.argv)>1 else os.getcwd()

print movie_dir
