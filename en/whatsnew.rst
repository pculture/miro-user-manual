====================
 What's new in Miro
====================

What's new in Miro 3.5
======================

Released on October 21st, 2010.

New features:

1. **Conversions**

   Miro allows you to easily convert media to other video/audio
   formats for your media devices.

   .. SCREENSHOT
      Screenshot of conversions tab with conversions going.

   .. image:: _static/whatsnew_3_5_conversions.png

2. **Improved Library Management**

   Improvements in tab display, item views, and queued download
   handling.

3. **Better HTTP downloading performance**

   We switched to using libcurl for HTTP downloading which is less
   CPU-intensive and works faster.

4. **HTTP auth digest**

   Miro now supports both HTTP auth basic and HTTP auth digest.

5. **Proxy authentication**

   Proxy authentication now works.

6. **Subtitle preferences**

   Specify font style (Windows) and encoding (Windows, GNU/Linux) to
   improve the display of subtitles.


Other changes:

1. Lots of work on the user interface to make it better.

2. Performance fixes for torrent restarting, proxy/http
   authentication, and database usage.

3. Cancel queued auto-downloads.

4. Remember tab views.

5. Moved things around in the directory layout of the source tree:

   ==================  ========
   Old path            New path
   ==================  ========
   platform/windows/   windows/
   platform/gtkx11/    linux/
   platform/osx/       osx/
   portable/           lib/
   ==================  ========

6. (GNU/Linux) Movies directory defaults to ``~/Videos/Miro`` per the
   Free Desktop specification.

7. (OSX) Updated the OSX build environment to be based on Python 2.6.

8. (OSX) Dropped support for OSX 10.4.

9. (Windows) Updated the Windows build environment to be based on
   Python 2.6 and Visual Studio 2008.

10. A lot of bug fixes.

See the `release notes for Miro 3.5 <https://develop.participatoryculture.org/index.php/3.5ReleaseNotes>`_.


What's new in Miro 3.0.3
========================

Released on July 26th, 2010.

Miro 3.0.3 is a bugfix release.

See the `release notes for Miro 3.0 <https://develop.participatoryculture.org/index.php/3.0ReleaseNotes>`_.


What's new in Miro 3.0.2
========================

Released on May 23rd, 2010.

Miro 3.0.2 is a bugfix release.

See the `release notes for Miro 3.0 <https://develop.participatoryculture.org/index.php/3.0ReleaseNotes>`_.


What's new in Miro 3.0.1
========================

Released on April 13th, 2010.

Miro 3.0.1 is a bugfix release.

See the `release notes for Miro 3.0 <https://develop.participatoryculture.org/index.php/wiki/3.0ReleaseNotes>`_.


What's new in Miro 3.0
======================

Released on March 23rd, 2010.

New features:

1. **Subtitle support.**  Miro now supports subtitle tracks, subtitle
   sidecar files and selecting external subtitle files.

   .. SCREENSHOT
      Screenshot of subtitle menu showing tracks.

   .. image:: _static/whatsnew_3_0_subtitles_support.png

2. **Play externally context-menu item.** The context-menu allows you
   to easily play media items in an external player.  The external
   player chosen will be whatever your operating system is set up to
   associate with that file type.

   .. SCREENSHOT
      Screenshot of Play Externally context-menu item.

   .. image:: _static/whatsnew_3_0_play_externally_menu.png

3. **Play externally preference.** You can opt to play all files using
   the external player.

   .. SCREENSHOT
      Screenshot of Play in Miro. preference.

   .. image:: _static/whatsnew_3_0_play_externally_preference.png

4. **Edit item dialog.** Allows you to edit titles, descriptions and
   media types for media items in the library.

   .. SCREENSHOT
      Screenshot of Edit Item dialog.

   .. image:: _static/whatsnew_3_0_edit_item_dialog.png

5. **Volume goes to 11.** We tweaked the volume control so the max
   volume is 200% on Windows and 300% on GNU/Linux and OSX.

Other changes:

1. (GTKX11) Removed support for Xine renderer.

2. (GTKX11) Support for media keys.

3. Performance fixes for first time startup experience, deleting
   folders of feeds, creating and updating large feeds, and adding
   items to a watched folder.

See the `release notes for Miro 3.0 <https://develop.participatoryculture.org/index.php/3.0ReleaseNotes>`_.
