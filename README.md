# `$ cmemo`
A command line clipboard manager written in Python.

This clipboard manager is intended to be used without opening any additional screen.
Once setup the only required step is to hit a key combination to save the current contents of the clipboard for later use.

## Dependencies
`pyperclip` python package is required. This package will be installed on running `setup.py`. If you experience trouble then use the `requirements.txt` file instead to manually install the dependencies.

*On some Linux distros `xclip` package may be required.* Install it with `sudo apt-get install xclip` on Ubuntu if you cannot save memos.

## Installation
* Git clone this repo and run the `setup.py`.

* Now bind a key-combination to the `cmemo_direct` command to save memos directly with a single keystroke.

   For example, for Ubuntu follow the instructions [here](http://askubuntu.com/a/331632) and type `cmemo_direct` in the `Command` field.

## Usage
To see the help screen type:

```text
$ cmemo -h

usage: clipboard_memo <command> [<args>]
Available commands are:
    save     Save the contents of clipboard
    delete   Delete a memo
    ls 		 List all saved memos
    yank     Copy a memo to clipboard

Save clipboard data as memos

positional arguments:
  command     Subcommand to run

optional arguments:
  -h, --help  show this help message and exit
```

## Todo
* Move from `pickle` to `sqlite3`

## License
MIT
