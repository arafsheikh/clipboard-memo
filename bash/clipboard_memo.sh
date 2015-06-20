function clipboard_memo() {
    
    currdir=`pwd`
    cd ~/.clipboard_memo/

    python memo.py $1 $2
    cd "$currdir"
}
