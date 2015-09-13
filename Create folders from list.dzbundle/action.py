# Dropzone Action Info
# Name: Folderlist
# Description: Drop list onto action to create folders at the location
# Handles: Files, Text
# Creator: Lars
# URL: www.systemic.de
# Events: Dragged, Clicked
# ---- Clicked disabled
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: No
# Version: 1.0
# MinDropzoneVersion: 3.0
# OptionsNIB: ChooseFolder

import time
import os, sys

#----------------------------------------------------------------------------------------------
# globals 
#----------------------------------------------------------------------------------------------

dir = "/Users/larsschulz/Desktop"
text = ""
data = ""

#----------------------------------------------------------------------------------------------
# helper functions
#----------------------------------------------------------------------------------------------

def my_dir():
    '''Get the path'''
    global dir
    # https://docs.python.org/2/library/os.path.html
    dir = os.path.dirname( items[0] )
    print dir

def cleanup():
    # TODO implement
    global data


def read_text_clip():
    global data
    data = dz.read_clipboard().splitlines()

def read_text():
    global data, text
    text = open(items[0], "r")
    data = text.read().splitlines()
    print "data: ", data
    print "data 1: ", data[0]


def create_folder():
    global data
    count = 1

    for data in data:
        # progress
        print count
        print len(data[0])

        count += 1
        dz.percent( count/len(data[0]) * 100)
        current_name = dir + "/" + data
        print current_name
        if not os.path.exists(current_name):
            os.makedirs(current_name)
#----------------------------------------------------------------------------------------------
#  Actions
#----------------------------------------------------------------------------------------------

def dragged():
    # Do Action
    my_dir()
    read_text()
    create_folder()

    # Notify completion
    dz.finish("Folders created.")
 
def clicked():
    global dir
    # TODO: Set dir dynamically at finder selection

    # Use clipboard content for folder creation
    read_text_clip()
    create_folder()

    # Notify completion
    dz.finish("Folders created from clipboard.")
    dz.url(False)
