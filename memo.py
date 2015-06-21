"""
A command line clipboard manager
"""
from pyperclip import copy, paste
import cPickle as pickle
import argparse, sys

try:
    MEMOS = pickle.load(open('dump.p', 'rb'))   #Load saved MEMOS
except IOError:
    #If dump doesn't exist create new
    MEMOS = []

class ClipboardMemo(object):

    def __init__(self):

        parser = argparse.ArgumentParser(
            description='Save clipboard data as MEMOS',
            usage='''clipboard_memo <command> [<args>]
Available commands are:
    save     Save the contents of clipboard
    delete   Delete a memo
    retrive  Display all saved MEMOS
    yank     Copy a memo to clipboard
''')
        parser.add_argument('command', help='Subcommand to run')
        args = parser.parse_args(sys.argv[1:2]) #Parse only the first argument

        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)

        #Execute the given command
        getattr(self, args.command)()

    @staticmethod
    def commit():
        """Save the current MEMOS to memory."""
        pickle.dump(MEMOS, open('dump.p', 'wb'))

    def save(self):
        """Save a new memo to the MEMOS list."""
        text = str(paste()) #Data from clipboard
        if not bool(text):
            exit()  #Nothing to save

        text = text.encode('utf-8') #Clean string
        text = text.strip() #Get rid of whitespaces
        MEMOS.append(text)
        self.commit()

    def delete(self):
        """Deletes the MEMOS of the given index number."""
        parser = argparse.ArgumentParser(
            description='Delete memo of the given index number from clipboard')
        parser.add_argument('index', type=int)
        args = parser.parse_args(sys.argv[2:])

        try:
            del MEMOS[args.index - 1]   #Since we enumerate from 1 instead of 0
        except TypeError:
            print 'Integer required'
        self.commit()

    @staticmethod
    def retrive():
        """Retrivs all saved MEMOS."""
        print '\n'.join(str(i) for i in enumerate(MEMOS, start=1))

    @staticmethod
    def yank():
        """Copy the memo corresponding to the given index number to clipboard."""
        parser = argparse.ArgumentParser(
            description='''Copy the memo corresponding to the given index number
                to clipboard''')
        parser.add_argument('index', type=int)
        args = parser.parse_args(sys.argv[2:])

        try:
            copy(str(MEMOS[args.index - 1]))    #Since we enumerate from 1 instead of 0
        except TypeError:
            pass    #Oops

if __name__ == '__main__':
    ClipboardMemo()
    