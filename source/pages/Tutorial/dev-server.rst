Setting Up a Development Game Server
====================================

Requirements
------------

* A C++17 or later compiler (e.g., Visual Studio or GCC)
* CMake
* vcpkg
* Git
* A method to launch the game client (see supported methods below)

Cloning the Repository
----------------------

To clone the server repository, run the following command:

    ``git clone --depth=1 https://github.com/decompfrontier/server``

Setting Up vcpkg
----------------

Clone the `vcpkg repository <https://github.com/microsoft/vcpkg>`_ and bootstrap vcpkg with metrics disabled:

    ``bootstrap-vcpkg -disableMetrics``

.. admonition:: Windows-Only Extra Steps

    On Windows, open an elevated Command Prompt and run the following command in your vcpkg directory:

    ``vcpkg integrate install``

Next, set up a system or user environment variable named ``VCPKG_ROOT`` pointing to your vcpkg installation directory.

Setting Up the Server
---------------------

Using CMake, select the preset ``Development config for XXXXX (64-bit)`` based on your operating system. Alternatively, use one of these commands:

- ``cmake --preset debug-win64`` (Windows)

- ``cmake --preset debug-lnx64`` (Linux)

- ``cmake --preset debug-osx64`` (macOS)

Configure and generate the target project. After building, you’ll get a binary named ``gimuserverw``. This is your development server executable, which you can run and debug to implement new features.

Download the assets from `21900.zip <https://drive.google.com/file/d/1ApVcJISPovYuWEidnkkTJi_NI8sD1Xmx/view>`_ and place them in the ``server repository/deploy/system/game_server`` directory. If this folder doesn’t exist, create it.

Extract ``assets.zip`` from ``21900.zip`` as shown below:

.. image:: ../../images/archive_21900.png

Open ``assets.zip`` and extract the ``content`` and ``mst`` folders into ``deploy/game_content``:

.. image:: ../../images/assets_zip.png

After extraction, you should have two folders, ``content`` and ``mst``, inside ``game_content``:

.. image:: ../../images/servercontent_root.png

The ``content`` folder should contain the following assets:

.. image:: ../../images/servercontent_content.png

The ``mst`` folder should contain these assets:

.. image:: ../../images/servercontent_mst.png

To modify the server configuration, edit the JSON files in the ``system`` directory. You can also adjust additional settings in ``gimuconfig.json`` and tweak Drogon-specific options in ``config.json``.

Your environment is now ready for developing the Brave Frontier emulator!
