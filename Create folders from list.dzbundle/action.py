# Dropzone Action Info
# Name: Folderlist
# Description: Drop list onto action to create folders at the location
# Handles: Files, Text
# Creator: Lars
# URL: www.systemic.de
# Events: Dragged 
# ---- Clicked disabled
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: No
# Version: 1.0
# MinDropzoneVersion: 3.0
# OptionsNIB: ChooseFolder

import time
import os, sys

# globals
dir = "/Users/larsschulz/Desktop"
text = ""
data = ""


# helpers
def my_dir():
	'''Get the path'''
	global dir
	# https://docs.python.org/2/library/os.path.html
	dir = os.path.dirname( items[0] )
	print dir

def read_text_clip():
    global text
    text = dz.read_clipboard()
    print text

def read_text():
    global data, text
    text = open(items[0], "r")
    data = text.read().splitlines()
    print "data: ", data
    print "data 1: ", data[0]

def create_folder():
    global data
        
    my_dir()
    read_text()
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

# Function for dragged text
def dragged():
    # Notify action
    dz.begin("Creating folders")

    # Do Action 
    create_folder()

    # Notify completion
    dz.finish("Folders created")
 
def clicked():
    # TODO: Use clipboard content for folder creation
    print dz.read_clipboard()
    dz.finish("Drop textfile onto action!")
    dz.url(False)
