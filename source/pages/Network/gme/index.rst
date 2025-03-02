Game Server
===================

The game server (gme) is the main server which all the actions of Brave Frontier are done.

The original server was written in PHP (according to a leak of one misconfigured file) as a REST api, 
each key of the JSON are not written in plaintext, rather they seems to be an hash of the field name,
this is presumably done to complex the analysis of the packets.


The flow of a gme packet works this file: (apply the opposite for reading one)

.. info::

    The AES cryptation key changes based from the Game request.

.. image::
    ../../../images/gme_flow.png

1. The actual JSON packet gets created by the client
2. The packet is crypted with AES/ECB and encoded in Base-64 with a key that changes for every request type
3. The crypted JSON is then embedded in a GME JSON


This is what a completed GME packet looks like:

.. code::
    
    {
    "F4q6i9xe": {
        "aV6cLn3v": "Client ID that send the request",
        "Hhgi79M1": "Game request"
    },
    "a3vSYuq2": {
        "Kn51uR4Y": "Crypted JSON body"
    }
    }

.. toctree::
    :caption: Game Server
    :name: toc-network-gme
    :maxdepth: 1

