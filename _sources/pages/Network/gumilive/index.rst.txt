Gumi Live
=================================

The Gumi Live API server is a server called in Brave Frontier
before the connection to the actual game server.
This server is the first to be called by the game (during the login screen).

This server is responsable for the following things:

*    The initial dynamic BF background
*    Version checking during startup (and optionally showing maintenance)
*    Guest account login
*    Facebook account login
*    Telling the game which account server and game server to connect

.. toctree::
    :caption: Gumi Live
    :name: toc-network-gumilive
    :maxdepth: 1

    DLS
    Account
