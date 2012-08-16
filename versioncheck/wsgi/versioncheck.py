import os
import site

wsgidir = os.path.dirname(__file__)
for path in ['../..']:
    site.addsitedir(os.path.abspath(os.path.join(wsgidir, path)))

from update import application
