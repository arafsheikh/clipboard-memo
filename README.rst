``$ cmemo``
===========

A command line clipboard manager written in Python.

This clipboard manager is intended to be used without opening any
additional screen. Once setup the only required step is to hit a key
combination to save the current contents of the clipboard for later use.

.. image:: https://landscape.io/github/arafsheikh/clipboard-memo/master/landscape.svg?style=flat
   :target: https://landscape.io/github/arafsheikh/clipboard-memo/master
   :alt: Code Health

Dependencies
------------

``pyperclip`` python package is required. This package will be automatically installed.

*On some Linux distros ``xclip`` package may be required.* Install it
with ``sudo apt-get install xclip`` on Ubuntu if you cannot save memos.

Installation
------------

-  Using Pypi, ``pip install clipboard_memo``

-  Now bind a key-combination to the ``cmemo_direct`` command to save
   memos directly with a single keystroke.

For example, for Ubuntu follow the instructions `here`_ and type
``cmemo_direct`` in the ``Command`` field.

Usage
-----

To see the help screen type:

.. code:: text

    $ cmemo -h

    usage: clipboard_memo <command> [<args>]
    Available commands are:
        save                Save the contents of clipboard
        delete INDEX        Delete a memo of given index number
        delete -a | --all   Delete all saved memos
        ls                  List all saved memos
        yank INDEX          Copy a memo to clipboard

    Save clipboard data as memos

    positional arguments:
      command     Subcommand to run

    optional arguments:
      -h, --help  show this help message and exit

Todo
----

-  Move from ``pickle`` to ``sqlite3``
-  Add colors
-  Shrink multi-line memos

License
-------

MIT

.. _here: http://askubuntu.com/a/331632
