# chardet's setup.py
from distutils.core import setup
setup(
    name = "django-audioplayer",
    packages = ["audioplayer"],
    version = "0.2.2",
    description = "A Django application for integrating a Flash based mp3 audioplayer into templates.",
    author = "Andres Reyes Monge",
    author_email = "armonge@gmail.com",
    url = "http://code.google.com/p/django-audioplayer/",
    keywords = ["django", "flash", "audio"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Framework :: Django",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: Libraries :: Python Modules",
        ],
    long_description = """
A Django application for integrating a Flash based mp3 audioplayer into
templates using a custom template tag. It uses the flashplayer from
http://www.1pixelout.net/code/audio-player-wordpress-plugin
and can be easily customized by template parameters.

"""
)
