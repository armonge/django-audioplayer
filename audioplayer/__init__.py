"""_

###################
The audioplayer app
###################

A Django application for integrating a Flash based mp3 audioplayer into
templates using a custom template tag. It uses the flashplayer from
1pixelout_  and can be easily customized by template parameters.

.. _1pixelout: http://www.1pixelout.net/code/audio-player-wordpress-plugin

Download
========

The audioplayer app is only available as a tarball. It contains the Django
application and the flashplayer from 1pixelout_. Also note the Changelog_

- django_audioplayer-0.2.tgz_
- django_audioplayer-0.1.tgz_

.. _django_audioplayer-0.2.tgz: http://www.pyjax.net/download/django_audioplayer-0.2.tgz
.. _django_audioplayer-0.1.tgz: http://www.pyjax.net/download/django_audioplayer-0.1.tgz
    

Installation
============
To install the audioplayer app, follow these steps:

1. Unpack the downloaded tarball in your projects directory
2. Add myproject.audioplayer`` to your ``INSTALLED_APPS`` variable
3. Configure your webserver or ``urls.py`` to serve the Flash file
   ``player.swf`` found in the ``media/audioplayer`` subdirectory. By
   default the player is searched at
   ``{{ MEDIA_URL }}/audioplayer/player.swf`` but that can be changed
   (see below).

That's it. The audioplayer does not use any models or views, only a custom
template tag named ``audioplayer``.  

Using the audioplayer template tag
==================================
The audioplayer can be used in any template like this::

    {% load audioplayer %}
    # ...
    {% audioplayer file=file_url %}
    # ...

First load the audioplayer template tag library, then instantiate the player
as often as you like, using different files and/or player configurations.

Here's a live example:

Customizing the audioplayer
===========================
The audioplayer can be customized to fit your project's needs.You can set
looping, width, height and the colors for the various player areas like
this::

    {% audioplayer file=file_url,loop=True,autostart=True,bg=0xff000 %}

The following table contains the full list of supported parameters. The
original can be found at 1pixelout_runtime_. Please be aware that the
original values for the ``autostart`` and ``loop`` has been *pythonified*:
Instead of using ``yes`` and ``no`` the ``audioplayer`` tag can also use
``False`` and ``True``.

.. _1pixelout_runtime: http://www.1pixelout.net/code/audio-player-wordpress-plugin/#runtime
  
============== ========== ===================================================
Parameter      Default    Description
============== ========== ===================================================
file           -          The URL of the mp3 file
playerUrl      see below  The URL of the player.swf file
autostart      False      The player will automatically open and start to
                          play the track (False|True)
loop           False      The track will be looped indefinitely (False|True)
bg             0xHHHHHH   Background colour option (where HHHHHH is a valid
                          hexadecimal colour value such as FFFFFF or 009933)
bgcolor        0xHHHHHH   Background colour
leftbg         0xHHHHHH   Left background colour
rightbg        0xHHHHHH   Right background colour
rightbghover   0xHHHHHH   Right background colour (hover)
lefticon       0xHHHHHH   Left icon colour
righticon      0xHHHHHH   Right icon colour
righticonhover 0xHHHHHH   Right icon colour (hover)
text           0xHHHHHH   Text colour
slider         0xHHHHHH   Slider colour
loader         0xHHHHHH   Loader bar colour
track          0xHHHHHH   Progress track colour
border         0xHHHHHH   Progress track border colour
width          156        The width of the player 
height         18         The height of the player

============== ========== ===================================================

Serving the Flash player
========================
By default the audioplayer tag uses the player.swf found at 
``{{ MEDIA_URL }}/audioplayer/player.swf``.

To change that behaviour pass the URL of the player using the ``playerUrl``
parameter like this::

    {% audioplayer file=file.mp3,playerUrl=/foo/bar/player.swf,loop=True %}
    

Inserted code
=============
The following code is inserted by the ``audioplayer`` template tag based on the
``audioplayer/audioplayer.html`` template (the shown code is just an example and
varies depending on your parameters)::

    <object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" width="180" height="60">
        <param name="width" value="180" />
        <param name="height" value="60" />
        <param name="bgcolor" value="f2f2f2" />
        <param name="flashvars" value="height=18&amp;bg=0xF7F7F7&amp;slider=0xB29461&amp;track=0xFFFFFF&amp;righticon=0x666666&amp;lefticon=0x666666&amp;soundFile=%2Fmedia%2Faudio%2FSuitcase_-_Sheep.mp3&amp;loader=0xEEFFCC&amp;rightbg=0x22C1D6&amp;bgcolor=0xf2f2f2&amp;rightbghover=0x32D1E6&amp;autostart=no&amp;text=0x4F4F4F&amp;leftbg=0xBAFF7B&amp;righticonhover=0x444444&amp;border=0x00FF00&amp;width=156&amp;loop=no" />
        <param name="src" value="/media/cms/audioplayer/player.swf" />
        <embed type="application/x-shockwave-flash" width="180" height="60" bgcolor="f2f2f2" flashvars="height=18&amp;bg=0xF7F7F7&amp;slider=0xB29461&amp;track=0xFFFFFF&amp;righticon=0x666666&amp;lefticon=0x666666&amp;soundFile=%2Fmedia%2Faudio%2FSuitcase_-_Sheep.mp3&amp;loader=0xEEFFCC&amp;rightbg=0x22C1D6&amp;bgcolor=0xf2f2f2&amp;rightbghover=0x32D1E6&amp;autostart=no&amp;text=0x4F4F4F&amp;leftbg=0xBAFF7B&amp;righticonhover=0x444444&amp;border=0x00FF00&amp;width=156&amp;loop=no" src="/media/cms/audioplayer/player.swf"></embed>
    </object>

Replacing the default code template
-----------------------------------
The code shown above is read from the template ``audioplayer/audioplayer.html``.
You can provide a custom template to adopt the code to your needs. The
template will be passed the following context variables:

player_url
    The URL of the audioplayer.
width
    The width of the player.
height
    The height of the player.
bgcolor
    The background color of the player.
flash_vars
    The flashvars for the player.
    

Alternatives
============

JavaScript
----------
Instead of integrating the audioplayer using a template tag one could also use
some JavaScript to add the player to the page. The easiest way to achieve this
is to use the jQuery_ and the jQuery plugin jMP3_.

.. _jQuery: http://www.jquery.com
.. _jMP3: http://www.sean-o.com/jquery/jmp3/

Other Flash players
-------------------
Besides the nice player from 1pixelout_, there are several other Flash based
audioplayers out on the web. Here's a list of them:

* http://1bit.markwheeler.net/
* http://www.sean-o.com/jquery/jmp3/
* http://jeroenwijering.com/?item=Flash_Single_MP3_Player

Changelog
=========

0.2
---
- The audioplayer is now really searched at
  ``{{ MEDIA_URL }}/audioplayer/player.swf`` as described in the documentation
  above.
- The parameters ``autostart`` and ``loop`` are now pythonified as
  described in the documentation above. Any of ``no,false,False,yes,true,True``
  can be used.
- The inserted ``<object>`` code is now based on the template
  ``audioplayer/audioplayer.html``.
 
0.1
---
Initial release.
 
"""
__docformat__ = "restructuredtext en"
