# Dropzone Action Info
# Name: Folderlist
# Description: Drop list onto action to create folders at the location
# Handles: Files, Text
# Creator: Lars
# URL: www.systemic.de
# Events: Clicked, Dragged
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


def dragged():
    # Welcome to the Dropzone 3 API! It helps to know a little Python before playing in here.
    # If you haven't coded in Python before, there's an excellent introduction at http://www.codecademy.com/en/tracks/python

    # Each meta option at the top of this file is described in detail in the Dropzone API docs at https://github.com/aptonic/dropzone3-actions/blob/master/README.md#dropzone-3-api
    # You can edit these meta options as required to fit your action.
    # You can force a reload of the meta data by clicking the Dropzone status item and pressing Cmd+R

    # This is a Python method that gets called when a user drags items onto your action.
    # You can access the received items using the items global variable e.g.
    create_folder()

    # The above line will list the dropped items in the debug console. You can access this console from the Dropzone settings menu
    # or by pressing Command+Shift+D after clicking the Dropzone status item
    # Printing things to the debug console with print is a good way to debug your script. 
    # Printed output will be shown in red in the console

    # You mostly issue commands to Dropzone to do things like update the status - for example the line below tells Dropzone to show
    # the text "Starting some task" and show a progress bar in the grid. If you drag a file onto this action now you'll see what I mean
    # All the possible dz methods are described fully in the API docs (linked up above)
    dz.begin("Starting some task...")

    # Below line switches the progress display to determinate mode so we can show progress
    dz.determinate(True)

    # Below lines tell Dropzone to update the progress bar display
    #dz.percent(10)
    #time.sleep(1)

    # The below line tells Dropzone to end with a notification center notification with the text "Task Complete"
    dz.finish("Task Complete")

    # You should always call dz.url or dz.text last in your script. The below dz.text line places text on the clipboard.
    # If you don't want to place anything on the clipboard you should still call dz.url(false)
    dz.text("Here's some output which will be placed on the clipboard")
 
def clicked():
    # This method gets called when a user clicks on your action
    print dz.read_clipboard()
    dz.finish("Drop textfile onto action!")
    dz.url(False)
