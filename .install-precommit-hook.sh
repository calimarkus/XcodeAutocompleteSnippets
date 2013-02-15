#!/bin/sh
#
# Installs the pre-commit git hook
# which will automatically update the README.md
# and stage it for the current commit right before
# every actual commit
#

hookfile=".pre-commit.hook"
target=".git/hooks/pre-commit"
backupTarget=".git/hooks/pre-commit.backup"

# file existing options
cancel=false
overwrite=false
backup=false

# ask what to do with existing file
if [ -e "$target" ] || [ -h "$target" ]; then
    echo "A pre-commit hook already exists!"
    echo "[c]ancel, [o]verwrite or [b]ackup"
    while true; do
        read answer
        case $answer in
            "c" ) cancel=true; break;;
            "o" ) overwrite=true; break;;
            "b" ) backup=true; break;;
            *   ) continue ;;
        esac
    done
    
    if $overwrite; then
        rm $target
    fi

    if $backup; then
        mv $target $backupTarget 
        echo "Saved old hook as $backupTarget"
    fi
fi

# cancel or install
if $cancel; then
    echo "Canceled"
else
    cp $hookfile $target
    echo "Installed hook: $target"
fi


