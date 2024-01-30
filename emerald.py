import mushroomlib
import os
import shutil
import sys

working_directory = os.getcwd()
isRunning = True

def ls():
    global working_directory
    listdir = os.listdir(working_directory)
    for i in listdir:
        print(i)

def cd():
    global working_directory
    pathdir = input("Path: ")
    fullpath = working_directory + "/" + pathdir
    isdir = os.path.isdir(fullpath)
    if (isdir == True):
        working_directory = fullpath
    else:
        print("Directory not found")

def cd_parentdir():
    global working_directory
    working_directory = os.path.abspath(os.path.join(working_directory, os.pardir))

def pwd():
    global working_directory
    print(working_directory)

commands = {
"ls":ls,
"cd":cd,
"cd ..":cd_parentdir,
"pwd":pwd,
"m":mushroomlib.loadmod,
"loadmod":mushroomlib.loadmod,
"exit":exit,
}


def console():
    global working_directory
    global isRunning
    while isRunning:
        command = input(working_directory+" $ ")
        if command in commands:
            commands[command]()
        else:
            print("Command not found.")
