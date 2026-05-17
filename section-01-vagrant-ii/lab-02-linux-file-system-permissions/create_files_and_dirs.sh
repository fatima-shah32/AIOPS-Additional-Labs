#!/bin/bash

echo "Creating structure..."

mkdir -p ~/lab2/directory1
mkdir -p ~/lab2/directory2

touch ~/lab2/directory1/file1.txt
touch ~/lab2/directory2/file2.txt

echo "Setting permissions..."

chmod 744 ~/lab2/directory1/file1.txt
chmod 744 ~/lab2/directory2/file2.txt

chmod 755 ~/lab2/directory1
chmod 755 ~/lab2/directory2

echo "Setting ownership..."

chown $USER:$USER ~/lab2/directory1/file1.txt
chown $USER:$USER ~/lab2/directory2/file2.txt

echo "Final structure:"
ls -l ~/lab2
