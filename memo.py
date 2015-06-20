from pyperclip import copy, paste
import cPickle as pickle
import argparse, sys

try:
    memos = pickle.load(open('dump.p', 'rb'))   #Load saved memos
except IOError:
    #If dump doesn't exist create new
    memos = []

class ClipboardMemo(object):
    
    def __init__(self):

        parser = argparse.ArgumentParser(
            description='Save clipboard data as memos',
            usage = '''clipboard_memo <command> [<args>]
Available commands are:
    save     Save the contents of clipboard
    delete   Delete a memo
    retrive  Display all saved memos
    yank     Copy a memo to clipboard
''')
        parser.add_argument('command', help = 'Subcommand to run')
        args = parser.parse_args(sys.argv[1:2]) #Parse only the first argument

        if not hasattr(self, args.command):
            print 'Unrecognized command'
            parser.print_help()
            exit(1)

        #Execute the given command
        getattr(self, args.command)()

    def commit(self):
        """Save the current memos to memory"""
        pickle.dump(memos, open('dump.p', 'wb'))

    def save(self):
        """Save a new memo"""

        parser = argparse.ArgumentParser(
            description = 'Save new memo from clipboard')

        text = str(paste()) #Data from clipboard
        if not bool(text):
            exit()  #Nothing to save

        text = text.encode('utf-8') #Clean string
        text = text.strip() #Get rid of whitespaces
        memos.append(text)    
        self.commit()

    def delete(self):
        """Deletes the memos of the given index number"""

        parser = argparse.ArgumentParser(
            description = 'Delete memo of the given index number from clipboard')       
        parser.add_argument('index', type = int)
        args = parser.parse_args(sys.argv[2:])
        
        try:
            del memos[args.index - 1]   #Since we enumerate from 1 instead of 0
        except TypeError:
            print 'Integer required'
        self.commit()

    def retrive(self):
        """Retrivs all saved memos"""
        parser = argparse.ArgumentParser(
            description = 'Retrive all saved memos')
        
        print '\n'.join(str(i) for i in enumerate(memos, start = 1))

    def yank(self):
        """Copy the memo corresponding to the given index number
        to clipboard
        """
        parser = argparse.ArgumentParser(
            description = '''Copy the memo corresponding to the given index number
                to clipboard''')
        parser.add_argument('index', type = int)
        args = parser.parse_args(sys.argv[2:])
        
        try:
            copy(str(memos[args.index - 1]))    #Since we enumerate from 1 instead of 0
        except TypeError:
            pass    #Oops

if __name__ == '__main__':
    ClipboardMemo()
