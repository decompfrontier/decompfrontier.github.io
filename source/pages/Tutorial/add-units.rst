Adding Units from the Unit Images Found in Game Content
=========================================================

Requirements
-------------

* Launching the server atleast once to generate the ``gme.sqlite`` file.
* One of two python scripts intended to grab units from .png files
* Creating a ``unit`` folder for the scripts to iterate through.
* Modifying said scripts to change the directory to your ``unit`` folder AND ``gme.sqlite`` file.


Prep
------

Begin by launching the server if you haven't already.

.. note::

    For best results, delete the gme.sqlite file and let it regenerate with a fresh file.

Navigate to your Unit folder: ``..\server\deploy\game_content\content\unit\img``

.. important::

    If you don't see this folder, it's because you didn't download the extra files detailed in the Game Client Tutorial.

Sort this folder alphabetically and click the first unit: ``unit_ills_thum_10011.png`` (Vargas 2-Star)

Scroll all the way down to the last unit: ``unit_ills_thum_9850167.png`` (A blue-eyed, pink-haired girl), and Shift-Click to Select all units in-between both of these units.

.. warning::

    A warning here. The units after ``unit_ills_thum_9850167.png`` aren't base game units and will cause issues if loaded during this tutorial.

Right-click, and choose ``Copy``

Navigate to your desktop and create a new folder named ``Units``. Then open this folder.

Right-click and paste the copied units from earlier. (If all went well you'll see ``2,547 items`` at the bottom left of the folder)


Modifying the Python Script
-----------------------------

You can find the ``Unique units + Filler Units to Max Inventory script`` `here <https://drive.google.com/file/d/18yUeKckfL-s4T23mwFN0Xzys39qWbXO9/view?usp=sharing>`_.

Alternatively, you could just grab all unique units using the script located `here <https://drive.google.com/file/d/144PyuC_JELeKSQIybAcuU1TsqWeZ-LSQ/view?usp=sharing>`_.

.. note::

    Running either script will over-write any current unit data stored in the ``gme.sqlite``. Feel free to run them as much as you'd like.

The only modifications you'll have to do in these scripts is changing both directories to match your file structure set-up. (They are pretty much the same as what you may have).

Save the script after modifying the directories.

Run the script.


Done
-----

Now, Load the server and client.

You should get a ton of files being requested to load (That means it worked)

.. note::

    Thankfully the bulk download is a one time thing and you won't have to do it again unless you unistall your current version of the patched client.


.. toctree::

    Placeholder <Please modify and include this document in the current tutorial pages>
