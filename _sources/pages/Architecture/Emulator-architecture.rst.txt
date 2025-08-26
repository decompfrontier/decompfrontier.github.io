Emulator (Server) architecture
========================================

The emulator reimplements the following web servers:

* Gumi API Server (used for login and the main background)
* Brave Frontier Game Server (which acts as the main server for the game)
* CDN Asset Server (where the game downloads the assets from the server)

The emulator uses SQLite as a local database to store and access userdata.

The root directory contains the following projects:

* deploy
* game_frontend
* gimuserver
* standalone_frontend

deploy
-----------

This directory contains all the configuration and assets of the game server.

A configuration can be, for example, the current gacha banners that should be
showed in the game.

The configuration is stored in JSON format.

config.json
^^^^^^^^^^^^^^

This file contains the configuration of the web framework `Drogon <https://github.com/drogonframework/drogon>`_
that is used for the emulator.

More information about this file can be found in `Drogon's wiki <https://github.com/drogonframework/drogon/wiki/ENG-11-Configuration-File>`_


gimuconfig.json
^^^^^^^^^^^^^^^^^^

This file contains the general configuration of the server, here an user can modify
the server wallpaper, specific logging and provide a custom asset directory.

An example JSON looks like this::

    {
        "system":
        {
            "content_root": "./game_content",
            "gme_sqlite_path": "./gme.sqlite",
            "session_timeout" : 1200,
            "mst_root": "./system"
        },
        "server":
        {
            "wallpaper_banner" : "/wallpaper/title_logo20160401.jpg",
            "game_version": 21900,
            "notice_url": "http://ios21900.bfww.gumi.sg/pages/versioninfo"
        },
        "log":
        {
            "enable": true,
            "request_path": "log_req",
            "response_path": "log_res",
            "dlc_error_file": "dlc_404.txt"
        }
    }

+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field name       | Type        | Description                                                                                                                                                                           |
+==================+=============+=======================================================================================================================================================================================+
| content_root     | String      | Directory where the game assets are found                                                                                                                                             |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| gme_sqlite_path  | String      | Path to store the local SQLite database                                                                                                                                               |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| session_timeout  | Integer     | If the client does not perform any network activity after this timeout (in milliseconds) the server would consider the client to have crashed and logout the user from the server     |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| mst_root         | String      | Directory where the server MST configuration is contained                                                                                                                             |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| wallpaper_banner | String      | Path (inside the game_content directory) which controls which image to show during Brave Frontier login screen                                                                        | 
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| game_version     | Integer     | Version of the client, this number has to match with what the client expects or it might ask the user to update the game                                                              |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| notice_url       | String      | URL to show in the Terms and Usage page during the game login screen                                                                                                                  |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| log::enable      | Boolean     | Enables or disables logging of request/responses                                                                                                                                      |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| request_path     | String      | Directory to store the request logs                                                                                                                                                   |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| response_path    | String      | Directory to store the response logs                                                                                                                                                  |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| dlc_error_file   | String      | Path to store the log of any missing asset file                                                                                                                                       |
+------------------+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

system
^^^^^^^^^^

The system directory contains all the game configuration that is sent to the game client,
the are essentially MSTs that are transated in human form.

game_frontend
------------------

This project produces a shared library that will can be used to embed the offline mod server into the game.

On Android, this library is loaded during startup by using a modified version of the Android Java code.

On Windows, this library is loaded during startup by the `Offline proxy <https://github.com/decompfrontier/offline-proxy>`_ module.

standalone_frontend
----------------------

As debugging the server while being embedded inside the game client can be an hard task, the purpose of this
project is to generate a standalone executable that starts the `gimuserver` library for simplify the development
of the server.

gimuserver
-------------

This project contains the actual server source emulator built as a static library ready to be linked by extenal projects.
