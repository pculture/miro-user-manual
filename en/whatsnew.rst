====================
 What's new in Miro
====================


What's new in Miro 5
====================


Released on ZZZ xxrd, 201Z.

New features:

1. **Song information and Album art lookup**
   Clean up your music collection by automatically looking up 
   the Artist, correct title, and album name and artwork among other thing.  


2. **Hybrid Filter View**
   A clean view to group togther all your songs by Album and Artist.  
   Clean way to view video items by kind (Movies, Clips, Podcasts...)

3. **Quick fill option to get your music onto your device**


4. **Purchase music from eMusic**
   We've add eMusic to our list of store so you can grow you music collection.

See the `release notes for Miro 5.0
<https://develop.participatoryculture.org/index.php/5.0ReleaseNotes>`_.


What's new in Miro 4
====================

Released on May 23rd, 2011.

New features:

1. **Better user interface**

   We've gone through and cleaned up the interface making it easier
   to use, more intuitive, and prettier.

2. **Device syncing**

   Sync media in Miro with your Android devices as well as any other
   device that shows up as an external drive.

3. **Sharing and streaming to other devices**

   Miro can stream media to any DAAP client.  Additionally, you can
   stream media from any DAAP client to Miro.

4. **Amazon store access**

   Miro makes it easier to purchase music from the Amazon store and
   download it directly to Miro.

5. **Metadata extraction**

   Miro can extract metadata from media files like genres, album
   titles, track numbers, artists, ...

6. **Performance enhancements**

   We've implemented a variety of performance enhancements to make
   Miro smoother and faster to respond.

See the `release notes for Miro 4.0
<https://develop.participatoryculture.org/index.php/4.0ReleaseNotes>`_.


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


What's new in Miro 3
====================

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
