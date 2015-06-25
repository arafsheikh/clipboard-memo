# clipboard-memo
Command line clipboard manager written in Python.

This clipboard manager is intended to be used without opening any additional screen.
Once setup the only required step is to hit a key combination to save the current contents of the
clipboard for later use.

#Dependencies
`pyperclip` python package is required.

To install dependencies run:
`pip install -r requirements.txt`

#Installation
1. First clone this repo with:
`git clone https://github.com/arafsheikh/clipboard-memo.git`

2. Now set both the bash scripts as executable:
`chmod +x install.sh`
and
`chmod +x oneclick.sh`

3. Run `./install.sh`

4. Restart your terminal

5. Now bind a keycombination to `oneclick.sh`. 

   For example, for Ubuntu follow the instructions [here](http://askubuntu.com/a/331632) and type `~/.clipboard_memo/oneclick.sh` in the `Command` field.

#Usage
To see the help screen type:

```text
$ clipboard_memo -h

usage: clipboard_memo <command> [<args>]
Available commands are:
    save     Save the contents of clipboard
    delete   Delete a memo
    retrive  Display all saved memos
    yank     Copy a memo to clipboard

Save clipboard data as memos

positional arguments:
  command     Subcommand to run

optional arguments:
  -h, --help  show this help message and exit
```

#Todo
* Move from `pickle` to `sqlite3`

#License
MIT
