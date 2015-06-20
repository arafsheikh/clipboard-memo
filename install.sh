#!/bin/bash

mkdir ~/.clipboard_memo
cp memo.py ~/.clipboard_memo
cp oneclick.sh ~/.clipboard_memo

echo -ne "Adding 'clipboard_memo' command to your .bashrc\n"
cat bash/clipboard_memo.sh >> ~/.bashrc

